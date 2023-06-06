import unittest

from cvermeer.colors import Color


class TestColor(unittest.TestCase):

    def test_init_color(self):
        Color(14, 240, 228)

    def test_from_hexacode(self):
        color: Color = Color.from_hex("#0ef0e4")
        self.assertEquals(color.color, (14, 240, 228), "Hexacode parser failed")

    def test_to_hexacode(self):
        color: Color = Color(14, 240, 228)
        self.assertEquals(color.hex, "#0ef0e4")

    def test_to_cv_color(self):
        color: Color = Color(14, 240, 228)
        self.assertEquals(color.cv_color, (228, 240, 14))

    def test_random_color(self):
        color: Color = Color.random_color()
        self.assertNotEquals(color.color, Color.random_color(), "Unless you are very unlucky, random color does not work")
