
import numpy as np

def get_severity_category(mean_joint_space):
    if mean_joint_space >=0.36:
        return "Invalid X-ray"
    elif mean_joint_space >=0.25:
        return "Severe OA"
    elif mean_joint_space>=0.18:
        return "Moderate OA"
    elif mean_joint_space>=0.12:
        return "Mild OA"
    else:
        return "Healthy"

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
        return None,"No Detection"

    # Calculate mean joint space
    mean_joint_space = np.mean(joint_spaces)
    severity_category=get_severity_category(mean_joint_space)
    print("*********** Mean Joint Space in evaluation.py is:", mean_joint_space)
    print("*********** Category : ",severity_category)
    return mean_joint_space,severity_category
