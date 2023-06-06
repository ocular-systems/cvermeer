from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
from random import randint


@dataclass
class Color:
    r: int
    g: int
    b: int

    @property
    def color(self) -> Tuple[int, int, int]:
        return (self.r, self.g, self.b)

    @property
    def cv_color(self) -> Tuple[int, int, int]:
        return (self.b, self.g, self.r)

    @property
    def hex(self) -> str:
        return "#%02x%02x%02x" % self.color

    def from_hex(hexacode: str) -> Color:
        return Color(*tuple(int(hexacode.strip("#")[i : i + 2], 16) for i in (0, 2, 4)))

    def random_color() -> Color:
        return Color(randint(0, 255), randint(0, 255), randint(0, 255))
