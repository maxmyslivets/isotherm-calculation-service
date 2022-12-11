from io import BytesIO

from PIL import Image

from image_processing.isotherm import Isotherm


def get_isotherm(image: bytes) -> Isotherm:
    # TODO: get more takes for getting temperatures for all pixels
    img = Image.open(BytesIO(image))
    # TODO: img >> x,y,z arrays from cv
    # TODO: get contours from matplotlib
    isotherm = Isotherm()
    return isotherm
