from dataclasses import dataclass

import numpy

from cvermeer.colors import Color
from cvermeer.shapes import Point


@dataclass
class Widget:
    position: Point
    color: Color = Color(255, 255, 255)

    def draw(self, frame: numpy.ndarray) -> None:
        ...
