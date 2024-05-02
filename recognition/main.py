import threading
import os

import cv2
from deepface import DeepFace

# 0 is the arg that says which camera, if you have multiple and it's messing up, try messing with it.
cap = cv2.VideoCapture(0)

# W and H of video
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# We're going to use this to dictate how often we evaluate the face
counter = 0

face_match = False

# Define the file path to reference.jpg
file_path = "reference.jpg"

# Print the absolute path being used by cv2.imread()

absolute_path = os.path.abspath(file_path)
reference_img = cv2.imread(absolute_path)

def check_face(frame):
    global face_match
    try:       
        # We're just passing a copy to be safe. We want to avoid data races
        # For those who don't know, data races are basically when two threads 
        # are messing with an object at the same time. It creates issues
        pass
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else: 
            face_match = False
    except ValueError:
        face_match = False


while True:
    # Get return value (if it return something) and frame from our camera
    ret, frame = cap.read()
    if ret:
        # How often we evaluate...
        if counter % 30 == 0:
            # Comma is important because threads take a tuple. W/out comma, it would just pass element
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            # Taking our frame, put word MATCH at pos (20,450) in Hershey simplex, size 2, green, with thickness 3
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
        else: 
            # The color code is (B,G,R) for this btw, so no match is red
            cv2.putText(frame, "NO MATCH", (20, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)
    



    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

