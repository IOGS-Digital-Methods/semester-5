"""camera_flux.py
Basler Camera video flux display (OpenCV)
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from pypylon import pylon
import cv2
import numpy as np

COLOR_MODE = "Mono12"  # "BGR8" / "Mono12"

def get_screen_size():
    cv2.namedWindow("temp", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("temp", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Récupération de la taille de la fenêtre en plein écran
    x, y, w, h = cv2.getWindowImageRect("temp")
    cv2.destroyWindow("temp")
    return h, w
    

def main():
    # --- 
    height, width = get_screen_size()
    mode = 'z'
    
    # --- Initialisation de la caméra ---
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    converter = pylon.ImageFormatConverter()
    if COLOR_MODE == 'BGR8':
        # BGR8
        camera.PixelFormat = "BGR8"     # OpenCV displays in BGR
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    elif COLOR_MODE == 'Mono12':
        # Mono 12
        camera.PixelFormat = "Mono12"
        converter.OutputPixelFormat = pylon.PixelType_Mono16  # On convertit vers 16 bits
        converter.OutputBitAlignment = pylon.OutputBitAlignment_LsbAligned
    
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    print("Appuyez sur 'q' pour quitter")

    # --- Boucle d'acquisition ---
    while camera.IsGrabbing():
        grab = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grab.GrabSucceeded():
            # --- Get Image ---
            img = converter.Convert(grab)
            frame_raw = img.GetArray()
            
            
            # --- Processing ---
            if mode == 'a': # Canny
                if COLOR_MODE == 'Mono12':
                    # Conversion 12 bits → 8 bits
                    frame8 = (frame_raw / 16).astype(np.uint8)
                else:
                    frame8 = frame_raw
                # Canny
                final_output = cv2.Canny(frame8, 50, 150)
            else:
                if COLOR_MODE == 'Mono12':
                    # Conversion 12 bits → 8 bits
                    frame8 = (frame_raw / 16).astype(np.uint8)
                else:
                    frame8 = frame_raw
                final_output = frame8
            # Redimensionnement
            display = cv2.resize(final_output, (width//2, height//2))
            cv2.imshow("Flux Basler a2A1920", display)

            # --- Mode management ---
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('a'):
                mode = 'a'
            elif key == ord('z'):
                mode = 'z'
                                
            # --- Histogramme ---
            hist = cv2.calcHist([frame8],[0],None,[256],[0,256])
            hist_norm = cv2.normalize(hist, None, 0, 200, cv2.NORM_MINMAX)
            hist_img = np.full((200, 256), 255, dtype=np.uint8)

            for x in range(256):
                cv2.line(hist_img, (x, 200), (x, 200 - int(hist_norm[x])), 0, 1)

            cv2.imshow("Histogramme", hist_img)

        grab.Release()

    camera.StopGrabbing()
    camera.Close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
