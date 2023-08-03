from flask import Flask , render_template ,request , jsonify
import os
import io
from PIL import Image
import io, base64


app = Flask(__name__)
							
@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        img_bytes = request.files["image_file"].read()
        print(img_bytes)
        tall = float(request.form['Tall'])
        print(tall)
        image = Image.open(io.BytesIO(base64.decodebytes(bytes(img_bytes, "utf-8"))))
        return jsonify({"request_id": tall})

@app.route('/')
def default():
    return 'API Working'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
