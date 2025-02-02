import kagglehub
from data_loader import load_dataset
from inference import load_model, run_inference
from evaluation import calculate_joint_space
from process_detections import process_detections
# Load model
model_path = kagglehub.model_download("tensorflow/centernet-resnet/tensorFlow2/101v1-fpn-512x512")
model = load_model(model_path)

# Load dataset
dataset = load_dataset('D:/Annotated New/train/_annotations.coco.json', 'D:/Annotated New/train')

true_positives, false_positives, false_negatives = 0, 0, 0

# Run inference and compare results
for img, ground_truth_bboxes in dataset:
    detections = run_inference(model, img)
    print("Detections: ",detections)
    all_detections = process_detections(detections)
    # Process the detections
    print("Model Detections:", detections)
    print("Ground Truth Bounding Boxes:", ground_truth_bboxes)
    







