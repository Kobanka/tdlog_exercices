import unittest
from exo1 import Item


class Exo1Test(unittest.TestCase):
    def test_item_construction(self):
        item = Item(10, 20)
        self.assertEqual(20, item.weight)


if __name__ == '__main__':
    unittest.main()


'''
to run the test, run this command in the terminal:
python -m unittest exo1/test_exo1.py

or with

if __name__ == '__main__':
    unittest.main()
'''
