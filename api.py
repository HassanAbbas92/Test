from flask import Flask , render_template ,request , jsonify
import os
import io
from PIL import Image
import cv2


app = Flask(__name__)
							
@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        img_bytes = request.files["image_file"].read()
        tall = float(request.form['Tall'])
        image = Image.open(io.BytesIO(img_bytes))
        return jsonify({"request_id": tall})

@app.route('/')
def default():
    return 'API Working'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)