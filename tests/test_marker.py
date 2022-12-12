from dataclasses import FrozenInstanceError
from image_processing.marker import Marker


def test_isotherm_point():

    x, y, t = 25, 30, 24.3
    marker = Marker(x, y, t)

    assert marker.x == x
    assert marker.y == y
    assert marker.temperature == t
    assert marker.__repr__() == f"Marker(x={x}, y={y}, t={t})"
    try:
        marker.t = 0
        assert False, "Marker class is not read-only"
    except FrozenInstanceError:
        assert True
