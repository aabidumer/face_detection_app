import cv2
from PIL import Image,ImageEnhance
import numpy as np 

import constants

def detect_faces(image):
    """
    Detect faces using the given image
    Args:
        image (png, jpg, jpeg): [description]
    Returns:
        img, faces : Image with detected face outlined with a rectangle and count of faces detected
    """
    # Load HAAR Cascade file
    face_cascade = cv2.CascadeClassifier(constants.face_cascade_file_path)
    new_img = np.array(image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Draw rectangle around the faces
    for (x, y, w, h) in faces:
				 cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img,faces 