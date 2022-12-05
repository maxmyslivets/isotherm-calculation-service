from flask import Flask, jsonify, request, make_response
from PIL import Image

app = Flask(__name__)

@app.route("/getisotherm", methods=['POST'])
def post():

    image = request.files.get("image")
    
    print(f"UPLOAD FILES: {image}")

    img = Image.open(image.read())
    print(f"IMAGE SIZE: {img.size}")

    #responce = make_response(jsonify({"message": "Succesfull"}), 200,)
    #response.headers["Content-Type"] = "application/json"

    return jsonify({"message": "Succesfull"})
