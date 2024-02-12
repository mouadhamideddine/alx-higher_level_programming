#!/usr/bin/python3
""" BASE UNITTEST MODULE """
import unittest
from models.base import Base


class TestBaseinstanciation(unittest.TestCase):
    """test base module"""

    def setUp(self):
        """creating instances"""
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base()
        self.base4 = Base()

    def test_nb_check(self):
        """check if _nb_objects increases
        successfly with each instanciation"""
        self.assertGreater(self.base2.id, self.base1.id)
        self.assertGreater(self.base3.id, self.base2.id)
        self.assertGreater(self.base4.id, self.base3.id)

    def test_constructor_with_id(self):
        """Test if constructor initializes
        id attribute correctly when an id is provided."""
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)


if __name__ == '__main__':
    unittest.main()
