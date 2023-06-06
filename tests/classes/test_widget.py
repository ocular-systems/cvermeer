import unittest

from cvermeer.widgets import Widget
from cvermeer.shapes import Point


class TestWidget(unittest.TestCase):
    def test_init_widget(self):
        Widget(position=Point(0.5, 0.5))
