import unittest
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"


class SimpleTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()