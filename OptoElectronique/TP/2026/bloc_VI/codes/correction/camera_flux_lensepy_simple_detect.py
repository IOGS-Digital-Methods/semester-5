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
EXPOSURE_TIME = 10000
EXPOSURE_INC = 1000
MIN_AREA = 100              # Minimal area of an object
APPROX_FACTOR = 0.01        # Tolérance pour approxPolyDP

def detect_shape(cnt):
    area = cv2.contourArea(cnt)
    if area < MIN_AREA:
        return None, None

    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, APPROX_FACTOR * peri, True)
    n = len(approx)

    if n == 3:
        shape = "Triangle"
    elif n == 4:
        rect = cv2.minAreaRect(cnt)
        w, h = rect[1]
        if h == 0 or w == 0:
            shape = "Inconnu"
        else:
            ratio = max(w, h) / min(w, h)
            shape = "Carre" if 0.90 < ratio < 1.10 else "Rectangle"
    elif n == 5:
        shape = "Pentagone"
    elif n == 6:
        shape = "Hexagone"
    else:
        shape = f"{n}-gon"

    return shape, approx


def main():
    # ---
    height, width = get_screen_size()
    mode = 'z'
    # --- Find camera
    camera = init_first_camera('./config/camera_vi.ini')
    if camera is None:
        cv2.destroyAllWindows()
        return
    exposure_time = EXPOSURE_TIME
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
        frame_gray = cv2.cvtColor(frame8, cv2.COLOR_BGR2GRAY)
        gauss_output = cv2.GaussianBlur(frame_gray, (5, 5), 4)
        _, thresh_output = cv2.threshold(gauss_output, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 
        canny_output = cv2.Canny(thresh_output, 50, 200)
        contours, _ = cv2.findContours(canny_output, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        objects_output = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)
        
        for cnt in contours:
            shape, approx = detect_shape(cnt)
            if shape is None:
                continue

            cv2.drawContours(objects_output, [approx], -1, (255, 0, 0), 2)

            # Centre du contour
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(objects_output, shape, (cX - 30, cY),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        
        if mode == ord('1'):    # Gray
            final_output = frame_gray
        elif mode == ord('2'):  # Gauss
            final_output = gauss_output            
        elif mode == ord('3'):  # Thresh
            final_output = thresh_output         
        elif mode == ord('4'):  # Canny
            final_output = canny_output  
        elif mode == ord('5'):  # Final
            final_output = objects_output
        elif mode == ord('+'):
            exposure_time = exposure_time + EXPOSURE_INC
            camera.set_parameter('ExposureTime', exposure_time)
            print(f"Exposure time: {exposure_time}")
            mode = 'z'
        elif mode == ord('-'):
            exposure_time = exposure_time - EXPOSURE_INC
            camera.set_parameter('ExposureTime', exposure_time)
            print(f"Exposure time: {exposure_time}")
            mode = 'z'
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
