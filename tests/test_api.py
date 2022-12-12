from api import app
from base64 import b64encode
import json
from image_processing.isotherm import Isotherm

with open('tests/media/DJI_0258.JPG', 'rb') as file:
    binary_file = b64encode(file.read())

markers = json.dumps({"m1": [10, 10, 20], "m2": [20, 20, 15], "m3": [25, 25, 21.02]})


def test_get_isotherm_status_code():

    response_post = app.test_client().post("/get_isotherm", data={'image': binary_file, "markers": markers})
    assert response_post.status_code == 200

    response_get = app.test_client().get("/get_isotherm")
    assert response_get.status_code == 405


def test_get_isotherm_content():

    response = app.test_client().post("/get_isotherm", data={'image': binary_file, "markers": markers})

    assert "status" in response.json.keys()
    assert "isotherm" in response.json.keys()


def test_get_isotherm_parse():

    response = app.test_client().post("/get_isotherm", data={'image': binary_file, "markers": markers})
    isotherm = Isotherm(response.json["isotherm"])

    assert isotherm
