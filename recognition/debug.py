# yay

import os
import cv2

# Print the current working directory
print("Current working directory:", os.getcwd())

# Define the file path to reference.jpg
file_path = "reference.jpg"

# Print the absolute path being used by cv2.imread()
absolute_path = os.path.abspath(file_path)
print("Absolute file path:", absolute_path)

# Attempt to load the image
image = cv2.imread(file_path)

if image is None:
    print("Failed to load the image. Check if the file exists and the path is correct.")
else:
    print("Image loaded successfully.")