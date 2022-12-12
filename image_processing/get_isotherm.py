from io import BytesIO

from matplotlib.image import imread

from image_processing.isotherm import Isotherm
from image_processing.marker import Marker


def get_isotherm(image: bytes, markers: dict) -> Isotherm:

    # img = imread(url)
    # FIXME: read from a url
    #  изображение заливается на фронт, оттуда берем url и пихаем в post запрос
    # заглушка
    img = imread('tests/media/DJI_0258.JPG')

    markers_ = [Marker(*values) for marker, values in markers.items()]

    # TODO: img >> x,y,z arrays from cv
    # TODO: get contours from matplotlib
    isotherm = Isotherm()

    return isotherm
