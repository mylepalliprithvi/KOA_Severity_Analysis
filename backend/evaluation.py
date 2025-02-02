
import numpy as np

def calculate_joint_space(processed_detections):
    """
    Calculate the mean joint space width based on processed detections.

    Parameters:
    processed_detections (list): A list of detections with bounding boxes.

    Returns:
    float: Mean joint space width.
    """
    joint_spaces = []

    for detection in processed_detections:
        # Extract bounding box coordinates
        boxes = detection['box']
        # Assuming boxes are normalized [x_min, y_min, x_max, y_max]
        for box in boxes:
            x_min, y_min, x_max, y_max = box
            joint_space = abs(x_max - x_min)  # Calculate joint space width
            joint_spaces.append(joint_space)

    if not joint_spaces:
        print("No joint detected")
        return None

    # Calculate mean joint space
    mean_joint_space = np.mean(joint_spaces)
    print("Mean Joint Space in evaluation.py is:", mean_joint_space)
    
    return mean_joint_space
