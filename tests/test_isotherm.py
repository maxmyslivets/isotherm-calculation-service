from dataclasses import FrozenInstanceError
from image_processing.isotherm import Point, Isoline, Isotherm


def test_isotherm_point():

    x, y = 25, 30
    point = Point(x, y)

    assert point.x == x
    assert point.y == y
    assert point.__repr__() == f"Point({x}, {y})"
    try:
        point.x = 0
        assert False, "Point class is not read-only"
    except FrozenInstanceError:
        assert True


def test_isotherm_isoline():

    n = 10
    points = [Point(_, _) for _ in range(n)]
    level = 120
    isoline = Isoline(points, level)

    assert isoline.level == level
    assert isoline.__repr__() == f"Isoline (l={level}, n={n})"


def test_isotherm_isotherm():
    data = {
        120: [
            [[1, 1], [2, 2], [3, 3], [4, 4]],
            [[1, 1], [2, 2], [3, 3]]
        ],
        125: [
            [[10, 10], [30, 30], [40, 40]],
            [[15, 15], [22, 22], [35, 35], [55, 55]],
            [[80, 80], [88, 88], [90, 90], [80, 82]]
        ]
    }
    isotherm = Isotherm(data)
    assert len(isotherm.isolines) == 5
    assert isotherm.__repr__() == f"Isotherm (n=5)"

    for level in data.keys():
        for level_isoline in data[level]:
            isoline = Isoline([Point(x, y) for x, y in level_isoline], level)
            assert isoline in isotherm.isolines
