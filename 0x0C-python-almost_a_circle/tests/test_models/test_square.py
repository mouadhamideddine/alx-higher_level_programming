import unittest
from unittest.mock import patch
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):

    def test_attributes(self):
        square1 = Square(5, 2, 3, 1)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.x, 2)
        self.assertEqual(square1.y, 3)

    def test_area(self):
        square2 = Square(3)
        self.assertEqual(square2.area(), 9)

    def test_display(self):
        square = Square(4)
        expected_output = "\n\n ####\n ####\n ####\n ####\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            square.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        square4 = Square(2)
        square4.update(2, 3, 4, 5, 6)
        self.assertEqual(str(square4), "[Square] (2) 5/6 - 3")

    def test_str(self):
        square5 = Square(3, 4, 5, 6)
        self.assertEqual(str(square5), "[Square] (6) 4/5 - 3")

    def test_size_property(self):
        square6 = Square(4)
        square6.size = 7
        self.assertEqual(square6.size, 7)
        self.assertEqual(square6.width, 7)
        self.assertEqual(square6.height, 7)


if __name__ == '__main__':
    unittest.main()