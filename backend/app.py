from flask import Flask, request, jsonify
import os
from severity_predictor import determine_joint_space
from inference import load_model
import kagglehub
app = Flask(__name__)
from  flask_cors import CORS

CORS(app)

model_path = kagglehub.model_download("tensorflow/centernet-resnet/tensorFlow2/101v1-fpn-512x512")
model = load_model(model_path)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to the temp_images directory
    temp_image_path = os.path.join('temp_images', file.filename)
    file.save(temp_image_path)

    # Run your severity prediction logic
    mean_joint_space = determine_joint_space(temp_image_path, model)

    print('mean_joint_space in app.py (backend): ',mean_joint_space)
    print('JSON return:', jsonify({'mean_joint_space': mean_joint_space}))

    # Return the results as a JSON response
    return jsonify({'mean_joint_space':mean_joint_space}), 200

if __name__ == "__main__":
    app.run(debug=True)

