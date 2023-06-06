from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

import numpy

from .shape import Shape


@dataclass
class Point(Shape):
    x: float
    y: float

    def tuple(self) -> Tuple[float, float]:
        """Returns the tuple representation of a point.

        Returns:
            Tuple[float, float]: The tuple representation of the point.
        """
        return self.x, self.y

    def to_scale(self, frame: numpy.ndarray) -> Point:
        return Point(int(self.x * frame.shape[1]), int(self.y * frame.shape[0]))

    def from_scale(self, frame: numpy.ndarray) -> Point:
        return Point(self.x / frame.shape[1], self.y / frame.shape[0])
