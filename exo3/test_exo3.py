import unittest
import os
from exo3 import processLines


class TestExo3(unittest.TestCase):
    def test_input_1(self):
        base_dir = os.path.dirname(__file__)
        input1_path = os.path.join(base_dir, "sample/input1.txt")
        output1_path = os.path.join(base_dir, "sample/output1.txt")

        with open(input1_path) as input1:
            lines = input1.readlines()

        with open(output1_path) as output1:
            expected = output1.read()

        self.assertEqual(expected, processLines(lines))

    def test_input_2(self):
        base_dir = os.path.dirname(__file__)
        input2_path = os.path.join(base_dir, "sample/input2.txt")
        output2_path = os.path.join(base_dir, "sample/output2.txt")

        with open(input2_path) as input2:
            lines = input2.readlines()

        with open(output2_path) as output2:
            expected = output2.read()

        self.assertEqual(expected, processLines(lines))


if __name__ == '__main__':
    unittest.main()
