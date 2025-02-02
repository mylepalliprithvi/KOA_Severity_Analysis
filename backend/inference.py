import tensorflow as tf
from image_preprocessing import preprocess_image

def run_inference(model, img):
    input_tensor = preprocess_image(img)
    detections = model(input_tensor)
    return detections

def load_model(model_path):
    model = tf.saved_model.load(model_path)
    return model

