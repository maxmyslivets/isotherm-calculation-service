from api import app
from base64 import b64encode
from image_processing.isotherm import Isotherm

with open('E:/Wall.jpg', 'rb') as file:
    binary_file = b64encode(file.read())


def test_get_isotherm_status_code():

    # TODO: get more takes for getting temperatures for all pixels
    response_post = app.test_client().post("/get_isotherm", data={'image': binary_file})
    assert response_post.status_code == 200

    response_get = app.test_client().get("/get_isotherm")
    assert response_get.status_code == 405


def test_get_isotherm_content():

    # TODO: get more takes for getting temperatures for all pixels
    response = app.test_client().post("/get_isotherm", data={'image': binary_file})

    assert "status" in response.json.keys()
    assert "isotherm" in response.json.keys()


def test_get_isotherm_parse():

    # TODO: get more takes for getting temperatures for all pixels
    response = app.test_client().post("/get_isotherm", data={'image': binary_file})
    isotherm = Isotherm(response.json["isotherm"])

    assert isotherm
