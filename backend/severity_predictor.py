import cv2
import numpy as np
from inference import run_inference
from process_detections import process_detections
from evaluation import calculate_joint_space
import kagglehub

def determine_joint_space(image_path, model):
    # Load and preprocess the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at path: {image_path}")

    # Step 1: Run inference with the detection model
    detections = run_inference(model, image)
    print("Detections: ",detections)
    # Step 2: Process detections to get usable format
    processed_detections = process_detections(detections)
    print("Processed detections: ",processed_detections)

    # Step 3: Predict severity based on processed detections
    mean_joint_space = calculate_joint_space(processed_detections)
    print("Mean Joint Space in severity_predictor.py: ",mean_joint_space)
    return mean_joint_space

# Example usage:
if __name__ == "__main__":
    from inference import load_model
    model_path = kagglehub.model_download("tensorflow/centernet-resnet/tensorFlow2/101v1-fpn-512x512")
    model = load_model(model_path)
    
    image_path = "D:/Annotated New/test/4dc1459e-179_1610357875335_3_jpg.rf.69247f84f0f7bec6bc7d4a26e21bcc32.jpg"
    severity_results = determine_joint_space(image_path, model)
    
