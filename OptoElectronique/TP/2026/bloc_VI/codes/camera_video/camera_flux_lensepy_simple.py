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
DISPLAY_RATIO = 0.8
EXPOSURE_TIME = 30000


def main():
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
        if mode == ord('a'):    # Canny
            final_output = cv2.Canny(frame8, 100, 150)
        elif mode == ord('g'):  # Gaussian Blur
            final_output = cv2.GaussianBlur(frame8, (15, 15), 4)
        elif mode == ord('i'):  # Inverse image
            final_output = 255 - frame8
        elif mode == ord('c'):  # Inverse image
            final_output = frame8[:, :, [2, 1, 0]]
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
        elif key != 255:    # No key
            mode = key

    camera.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
