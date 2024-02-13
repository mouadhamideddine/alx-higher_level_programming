import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Test Rectangle instanciation and features"""
    def setUp(self):
        """instaciation method"""
        Base._Base__nb_objects = 0
        self.rectangle1 = Rectangle(5, 10)
        self.rectangle2 = Rectangle(6, 12, 4, 5)
        self.rectangle3 = Rectangle(6, 12, 4, 5, 3000)
        self.rectangle = Rectangle(10, 2)

    def test_id(self):
        """testing id's"""
        self.assertEqual(self.rectangle1.id, 1)
        self.assertEqual(self.rectangle2.id, 2)
        self.assertEqual(self.rectangle3.id, 3000)

    def test_placeholders(self):
        """testing class placesholders"""
        self.assertEqual(self.rectangle1.width, 5)
        self.assertEqual(self.rectangle1.height, 10)
        self.assertEqual(self.rectangle1.x, 0)
        self.assertEqual(self.rectangle1.y, 0)
        self.assertEqual(self.rectangle2.width, 6)
        self.assertEqual(self.rectangle2.height, 12)
        self.assertEqual(self.rectangle2.x, 4)
        self.assertEqual(self.rectangle2.y, 5)

    def test_width_valid(self):
        """test_width_valid"""
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_height_valid(self):
        """test_height_valid"""
        self.rectangle.height = 6
        self.assertEqual(self.rectangle.height, 6)

    def test_x_valid(self):
        """test_x_valid"""
        self.rectangle.x = 7
        self.assertEqual(self.rectangle.x, 7)

    def test_y_valid(self):
        """test_y_valid"""
        self.rectangle.y = 8
        self.assertEqual(self.rectangle.y, 8)

    def test_area(self):
        """test area"""
        self.assertEqual(self.rectangle.area(), 20)

    def test_display(self):
        """test display"""

        saved_stdout = sys.stdout
        sys.stdout = StringIO()
        self.rectangle.display()
        displayed_output = sys.stdout.getvalue()
        sys.stdout = saved_stdout
        expected_output = "##########\n" * 2
        self.assertEqual(displayed_output, expected_output)

    def test_update(self):
        """test update"""
        self.rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 4/5 - 2/3")

    def test_str(self):
        """test str"""
        self.assertEqual(str(self.rectangle1), "[Rectangle] (1) 0/0 - 5/10")


if __name__ == '__main__':
    unittest.main()
