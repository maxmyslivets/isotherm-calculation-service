from base64 import b64decode

from flask import Flask, request, jsonify

from image_processing.get_isotherm import get_isotherm as processing


app = Flask(__name__)


@app.route("/get_isotherm", methods=["POST"])
def get_isotherm():

    binary_file = request.form.to_dict()["image"]
    # TODO: get more takes for getting temperatures for all pixels
    isotherm = processing(b64decode(binary_file))

    return jsonify({'status': 'success', 'isotherm': isotherm.dict})


if __name__ == "__main__":
    app.run()
