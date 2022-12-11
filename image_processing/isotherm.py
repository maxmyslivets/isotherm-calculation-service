from dataclasses import dataclass


@dataclass()
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


@dataclass()
class Isoline:
    points: list[Point]
    level: float

    def __repr__(self) -> str:
        return f"Isoline (l={self.level}, n={len(self.points)})"


@dataclass
class Isotherm:
    data: dict
    isolines: list[Isoline] = None

    def __post_init__(self) -> None:
        # deserialize data to list[Isoline]
        pass

    def __repr__(self) -> str:
        return f"Isotherm (n={len(self.isolines)})"
