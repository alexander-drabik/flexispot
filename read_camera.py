import cv2
import numpy as np
import game

def highlight_black_pixels(image, threshold=30):
    mask = np.all(image < threshold, axis=-1)
    
    highlighted_image = image.copy()
    
    highlighted_image[mask] = [0, 0, 255]

    black_count = np.sum(mask)
    
    return highlighted_image, black_count

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Nie można otworzyć kamery")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Nie można odczytać klatki z kamery")
            break

        highlighted_frame, black_count = highlight_black_pixels(frame, threshold=100)
        print(black_count)

        cv2.imshow('Highlighted Camera Feed', highlighted_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        game.update(black_count)

finally:
    cap.release()
    cv2.destroyAllWindows()

