from dataclasses import dataclass

import numpy
import cv2 as opencv

from cvermeer.widgets import StaticWidget


@dataclass
class TextWidget(StaticWidget):
    text: str
    scale: float = 1.0
    thickeness: int = 1

    def draw(self, frame) -> None:
        opencv.putText(
            frame,
            f"{self.text}",
            self.position.tuple(),
            opencv.FONT_HERSHEY_PLAIN,
            self.scale,
            self.color.cv_color(),
        )
