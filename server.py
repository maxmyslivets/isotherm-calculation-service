from flask import Flask, request, jsonify
from PIL import Image
from base64 import b64decode
import  io


app = Flask(__name__)


@app.route("/im_size", methods=["POST"])
def process_image():
    binary_file = request.form.to_dict()["image"]
    img = Image.open(io.BytesIO(b64decode(binary_file)))

    return jsonify({'msg': 'success', 'size': [img.width, img.height]})


if __name__ == "__main__":
    app.run(debug=True)
