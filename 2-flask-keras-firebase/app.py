import numpy as np
from PIL import Image

import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from werkzeug.datastructures import FileStorage
from keras.models import model_from_json

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

import firebase

app = Flask(__name__)
api = Api(app, version="1.0", title="MNIST Classification", description="CNN Model trained from MNIST dataset")
ns = api.namespace('index')

single_parser = api.parser()
single_parser.add_argument("file", location="files", type=FileStorage, required=True)

# DON'T UPLOAD YOUR MODEL IN THE BODY OF YOUR ROUTE FUNCTION
# model will be loaded every time a request comes in
model = load_model('./model.h5')
graph = tf.get_default_graph()

firebase.config()

@ns.route('/prediction')
class CNNPrediction(Resource):
    """Uploads your data to the CNN"""
    @api.doc(parser=single_parser, description='Upload an mnist image')
    def post(self):
        args = single_parser.parse_args()
        image_file = args.file
        img = Image.open(image_file)
        
        image_resize = img.resize((28, 28))
        image = img_to_array(image_resize)
        x = image.reshape(1, 28, 28, 1)
        x = x / 255

        with graph.as_default():
            out = model.predict(x)

        prediction = np.argmax(out[0])

        firebase.add_to_firestore(image_file.filename, prediction)

        return {'prediction': str(prediction)}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
