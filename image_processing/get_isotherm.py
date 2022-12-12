from io import BytesIO

from PIL import Image

from image_processing.isotherm import Isotherm
from image_processing.marker import Marker


def get_isotherm(image: bytes, markers: dict) -> Isotherm:

    img = Image.open(BytesIO(image))
    markers_ = [Marker(*values) for marker, values in markers.items()]

    # TODO: img >> x,y,z arrays from cv
    # TODO: get contours from matplotlib
    isotherm = Isotherm()

    return isotherm
