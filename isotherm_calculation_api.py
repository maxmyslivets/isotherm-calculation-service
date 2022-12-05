from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route("/getisotherm", methods=['POST'])
def post():

    upload_files = request.files.getlist("file[]")
    print(f"UPLOAD FILES: {upload_files}")

    responce = make_response(jsonify({"message": "Succesfull"}), 200,)
    response.headers["Content-Type"] = "application/json"

    return response
