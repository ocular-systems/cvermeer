from dataclasses import dataclass
from datetime import datetime

from cvermeer.widgets import DynamicWidget, StaticWidget
from .text_widget import TextWidget


@dataclass
class TimeWidget(StaticWidget):
    label: str

    def draw(self, frame) -> None:
        TextWidget(
            self.position,
            self.color,
            f"{self.label} : {datetime.strftime(datetime.now(), '%H:%M::%S')}",
        ).draw(frame)
