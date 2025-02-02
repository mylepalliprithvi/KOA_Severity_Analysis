import os
import json
import cv2

def load_dataset(annotation_file, img_folder):
    data = []
    with open(annotation_file, 'r', encoding='utf-8') as f:
        annotation = json.load(f)
    
    for image_info in annotation['images']:
        img_name = image_info['file_name']
        img_path = os.path.join(img_folder, img_name)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Image {img_name} not found at {img_path}.")
            continue

        height, width = img.shape[:2]
        image_id = image_info['id']
        bboxes = []
        
        for ann in annotation['annotations']:
            if ann['image_id'] == image_id and ann['category_id'] == 1:  # Assuming '1' is the ID for 'knee'
                x_min, y_min, box_width, box_height = ann['bbox']
                x_max, y_max = x_min + box_width, y_min + box_height
                bboxes.append([x_min, y_min, x_max, y_max])

        data.append((img, bboxes))
    
    return data
