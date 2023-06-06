from __future__ import annotations
from dataclasses import dataclass

import numpy


@dataclass
class Shape:
    def to_scale(self, frame: numpy.ndarray) -> Shape:
        """Scale a floating point to the frame shape, and returns a Point with integer representation.

        Args:
            frame (numpy.ndarray): The shape on to project the points.

        Returns:
            Point: The scaled point.
        """
        ...

    def from_scale(self, frame: numpy.ndarray) -> Shape:
        """Downscale a point to it's frame proportion, for proportionnal representation on different frame sizes.

        Args:
            frame (numpy.ndarray): The frame from which the point was taken.

        Returns:
            Shape: The downscaled shape
        """
        ...
