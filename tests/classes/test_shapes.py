import unittest

from cvermeer.shapes import Point


class TestShapes(unittest.TestCase):
    def test_init_shape(self):
        Point(0.5, 0.5)

    def test_from_scale(self):
        raise NotImplementedError()

    def test_to_scale(self):
        raise NotImplementedError()
