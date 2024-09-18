from unittest import TestCase
import area

class TestArea(TestCase):
    def test_triangle_area(self):
        self.assertEqual(10, area.triangle_area(10, 20))

    def test_rectangle_area(self):
        self.assertAlmostEqual(17.7346, area.rectangle_area(7.25, 2.32))

    def test_negative_area_value_error(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-10, 0)

        with self.assertRaises(ValueError):
            area.triangle_area(0, -5)

        with self.assertRaises(ValueError):
            area.triangle_area(-10, -4)

    def test_base_and_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 0))
        self.assertEqual(0, area.rectangle_area(0, 2))
        self.assertEqual(0, area.rectangle_area(2, 0))