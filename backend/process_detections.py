def process_detections(detections):
    """Process detections to convert to a usable format."""
    processed_detections = []
    detection_boxes = detections['detection_boxes']
    detection_classes = detections['detection_classes']
    detection_scores = detections['detection_scores']
    
    for i in range(len(detection_boxes)):
        detection = {
            'box': detection_boxes[i].numpy().tolist(),  # Convert to numpy array, then to list
            'class': int(detection_classes[i][0].numpy().item()) if len(detection_classes[i]) > 0 else int(detection_classes[i].numpy().item()),  # Access first element if it's an array
            'score': float(detection_scores[i][0].numpy().item()) if len(detection_scores[i]) > 0 else float(detection_scores[i].numpy().item())  # Access first element if it's an array
        }
        processed_detections.append(detection)
    
    #print("Processed Detections Output: ",processed_detections)
    return processed_detections
