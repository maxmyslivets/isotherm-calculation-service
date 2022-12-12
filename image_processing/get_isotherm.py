from io import BytesIO

from matplotlib.image import imread

from image_processing.isotherm import Isotherm
from image_processing.marker import Marker


def get_isotherm(image: bytes, markers: dict) -> Isotherm:

    img = imread(BytesIO(image))    # FIXME: read from a url
    markers_ = [Marker(*values) for marker, values in markers.items()]

    # TODO: img >> x,y,z arrays from cv
    # TODO: get contours from matplotlib
    isotherm = Isotherm()

    return isotherm
