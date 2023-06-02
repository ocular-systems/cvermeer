from dataclasses import dataclass


@dataclass
class Shape:
    def draw(self) -> None:
        ...
