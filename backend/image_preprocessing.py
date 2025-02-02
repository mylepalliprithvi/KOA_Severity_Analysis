import cv2
import numpy as np

def preprocess_image(img, target_size=(512, 512)):
    img_resized = cv2.resize(img, target_size)
    img_normalized = img_resized / 255.0
    input_tensor = np.expand_dims(img_normalized, axis=0)
    return input_tensor
