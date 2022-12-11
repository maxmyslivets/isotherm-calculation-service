from api import app
from base64 import b64encode


def test_get_isotherm():
    with open('E:/Wall.jpg', 'rb') as file:
        binary_file = b64encode(file.read())
    response = app.test_client().post("/get_isotherm", data={'image': binary_file})

    assert response.status_code == 200
