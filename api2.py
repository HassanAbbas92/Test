from flask import Flask , render_template ,request , jsonify
import os
import io
from PIL import Image
import io, base64


app = Flask(__name__)
							
@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        img_bytes = request.form["image_file"]
        print(img_bytes)
        tall = float(request.form['Tall'])
        print(tall)
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(img_bytes, "utf-8"))))
        img.save('D:/Image/my-image.png')
        return jsonify({"blendshapes": [{"Skinny": "1","test": "0","M_Amari_African": "0.2"}]})

@app.route('/')
def default():
    return 'API Working'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
