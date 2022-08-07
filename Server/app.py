from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from genrax import predict

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
MODEL_PATH = 'genrax/models/model.h5'
SHAPE = (130, 20)

ALLOWED_EXTENSIONS = set(["wav", "mp3"])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file-upload', methods=['POST'])
def genraxAPI_says():

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request', "status code": 404})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 404
        return resp

    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading', "status code": 400})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 400

        return resp

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        uploaded_file = f"{UPLOAD_FOLDER}/{filename}"

        resp = {
            'message': 'File successfully uploaded',
            'status code': 201
        }

        resp["label"] = predict.predict(FILE_PATH=uploaded_file, MODEL_PATH=MODEL_PATH, SHAPE=SHAPE)
        resp = jsonify(resp)
        resp.headers.add('Access-Control-Allow-Origin', '*')

        os.remove(uploaded_file)

        return resp

    else:
        resp = jsonify({'message': 'Allowed file types are wav, mp3'})
        resp.status_code = 403

        return resp


@app.route('/')
def main():
    return render_template(["index.html"])

# port = int(os.getenv('PORT'))
port = 3000

if __name__ == '__main__':
    app.run(debug=True)

