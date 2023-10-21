from flask import Flask
from flask_restful import Api #import api
from flask_cors import CORS #configure cors
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__) #Create a new flask application
api = Api(app) 
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

photos = UploadSet("photos", extensions=("jpg"))
app.config["UPLOADED_PHOTOS_DEST"] = "path_to_upload_folder"
configure_uploads(app, photos)

#retrieve images
@app.route('/api/process_images', methods=['GET'])
def get_images()
    return jsonify(img)

#create (process) images
@app.route('/api/process_images', methods=['POST'])
def process_images():
    img = json.loads(request.data)

if __name__ == '__main__':
    app.run(debug=True)
