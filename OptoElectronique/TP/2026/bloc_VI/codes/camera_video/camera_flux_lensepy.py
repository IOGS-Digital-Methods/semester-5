"""camera_flux.py
Basler Camera video flux display (OpenCV)
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from pypylon import pylon
import cv2
import numpy as np

from lensepy.utils import get_screen_size
from lensepy.modules.basler.basler_models import init_first_camera

COLOR_MODE = "BayerRG8"  # "BayerRG8" / "Mono12"
GAUSS_SIZE = (15, 15)    # Taille du flou gaussien
GAUSS_SIGMA = 1.9
DISPLAY_RATIO = 0.66
EXPOSURE_TIME = 15000

clicked_x, clicked_y = None, None
need_slice = False
need_histo = False
slice_orientation = None  # 'h' pour horizontal, 'v' pour vertical

def mouse_callback(event, x, y, flags, param):
    global clicked_x, clicked_y, need_slice, need_histo, slice_orientation

    if event == cv2.EVENT_LBUTTONDOWN:      # clic gauche → coupe horizontale
        clicked_x, clicked_y = x, y
        slice_orientation = 'h'
        need_slice = True

    elif event == cv2.EVENT_RBUTTONDOWN:    # clic droit → coupe verticale
        clicked_x, clicked_y = x, y
        slice_orientation = 'v'
        need_slice = True

def main():
    global clicked_x, clicked_y, need_slice, need_histo, slice_orientation
    
    # --- 
    height, width = get_screen_size()
    mode = 'z'
    # --- Find camera
    camera = init_first_camera('./config/camera_vi.ini')
    if camera is None:
        cv2.destroyAllWindows()
        return
    # --- Camera parameters
    camera.set_parameter('PixelFormat', COLOR_MODE)
    camera.set_parameter('ExposureTime', EXPOSURE_TIME)
    # --- Start acquisition    
    camera.open()
    camera.camera_acquiring = True
    
    print("Appuyez sur 'q' pour quitter")
    
    # --- Boucle d'acquisition ---
    while camera.camera_acquiring:
        # --- Get Image ---
        frame_raw = camera.get_image()
        # --- Image conversion ---
        if COLOR_MODE == 'Mono12':
            # Conversion 12 bits to 8 bits
            frame8 = (frame_raw / 16).astype(np.uint8)
        elif COLOR_MODE == 'BayerRG8':
            frame8 = frame_raw
            frame8 = cv2.cvtColor(frame8, cv2.COLOR_BGR2RGB)
        else:
            frame8 = frame_raw
            
        # --- Processing ---
        if mode == 'a': # Canny
            #frame8 = cv2.GaussianBlur(frame8, GAUSS_SIZE, GAUSS_SIGMA)
            # Canny
            final_output = cv2.Canny(frame8, 50, 150)
        else:
            final_output = frame8
        
        # --- Image display ---
        max_w = int(width * DISPLAY_RATIO)
        max_h = int(height * DISPLAY_RATIO)
        h_src, w_src = final_output.shape[:2]
        scale = min(max_w / w_src, max_h / h_src)
        new_w = int(w_src * scale)
        new_h = int(h_src * scale)
        display = cv2.resize(final_output, (new_w, new_h))
        cv2.imshow("Flux Basler a2A1920", display)

        # --- Mode management ---
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            camera.camera_acquiring = False
            camera.close()
        elif key == ord('a'):
            mode = 'a'
        elif key == ord('z'):
            mode = 'z'
        elif key == ord('h'):   # h pour clear slice
            need_histo = not need_histo
            if not need_histo:
                cv2.destroyWindow("Histogram")
        elif key == ord('c'):   # c pour clear slice
            if need_slice:
                cv2.destroyWindow("Slice")
            need_slice = False
                   
        # --- Histogramme ---
        if COLOR_MODE == 'BayerRG8':
            frame_hist = cv2.cvtColor(frame8, cv2.COLOR_RGB2YUV)
        else:
            frame_hist = frame8

        if need_histo:
            hist = cv2.calcHist([frame_hist],[0],None,[256],[0,256])
            hist_norm = cv2.normalize(hist, None, 0, 200, cv2.NORM_MINMAX)
            hist_img = np.full((200, 256), 255, dtype=np.uint8)

            for x in range(256):
                value = int(hist_norm[x].item())
                cv2.line(hist_img, (x, 200), (x, 200 - value), 0, 1)

            cv2.imshow("Histogram", hist_img)
        
        # --- Slice Display ---
        if need_slice:
            # Convert coordinates from resized display back to original frame
            scale_x = frame8.shape[1] / (new_w)
            scale_y = frame8.shape[0] / (new_h)

            orig_x = int(clicked_x * scale_x)
            orig_y = int(clicked_y * scale_y)

            if slice_orientation == 'h':
                profile = frame_hist[orig_y, :, 0]
            elif slice_orientation == 'v':
                profile = frame_hist[:, orig_x, 0]

            factor = 2  # prendre 1 point sur 2
            profile_sampled = profile[::factor]
            profile_img = np.full((200, len(profile_sampled)), 255, dtype=np.uint8)
            prof_norm = cv2.normalize(profile_sampled, None, 0, 200, cv2.NORM_MINMAX)
            prof_norm = prof_norm.reshape(-1)

            for i, val in enumerate(prof_norm):
                v = int(float(val))
                cv2.line(profile_img, (i, 200), (i, 200 - v), 0, 1)

            cv2.imshow("Slice", profile_img)

    camera.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
