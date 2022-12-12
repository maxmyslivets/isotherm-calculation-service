from dataclasses import dataclass


@dataclass(frozen=True)
class Marker:
    x: int
    y: int
    temperature: float

    def __repr__(self) -> str:
        return f"Marker(x={self.x}, y={self.y}, t={self.temperature})"
