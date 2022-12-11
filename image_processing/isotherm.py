from dataclasses import dataclass, field


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


@dataclass(frozen=True)
class Isoline:
    points: list[Point]
    level: float

    def __repr__(self) -> str:
        return f"Isoline (l={self.level}, n={len(self.points)})"


@dataclass()
class Isotherm:
    isolines: list[Isoline] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Isotherm (n={len(self.isolines)})"

    @property
    def dict(self):
        isotherm_json = dict()
        for isoline in self.isolines:
            if isoline.level not in isotherm_json.keys():
                isotherm_json[isoline.level] = []
            points = [[point.x, point.y] for point in isoline.points]
            isotherm_json[isoline.level].append(points)
        return isotherm_json
