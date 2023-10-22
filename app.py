from flask import Flask, request, jsonify, send_file
from flask_cors import CORS  # Import CORS from flask_cors
from predictor import Predictor
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})



# Define the upload folder
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route('/api/process_images', methods=['POST'])
def process_images():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'Both images are required'}), 400

    file1 = request.files['image1']
    file2 = request.files['image2']

    st.write(f"Received image 1: {file1.filename}")
    st.write(f"Received image 2: {file2.filename}")

    file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1.filename))
    file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2.filename))

    query_image_path = os.path.join(
        app.config['UPLOAD_FOLDER'], file1.filename)
    reference_image_path = os.path.join(
        app.config['UPLOAD_FOLDER'], file2.filename)

    st.write(f"Query image path: {query_image_path}")
    st.write(f"Reference image path: {reference_image_path}")

    # Create a predictor object
    predictor = Predictor()

    st.write("Aligning the images...")

    # Align the images
    aligned_image = predictor.align_image_pair(
        query_image_path, reference_image_path)

    if aligned_image is not None:
        # Send the aligned image in the response
        st.write("Image alignment successful.")
        return send_file(aligned_image, mimetype='image/jpeg')
    else:
        st.write("Image alignment failed.")
        return jsonify({'error': 'Image alignment failed'}), 500


if __name__ == '__main__':
    app.run(debug=True)
