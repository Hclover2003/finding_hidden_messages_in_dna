import unittest
from utils import *


class SimpleTest(unittest.TestCase):
    # Returns True or False.
    def test_prof_prob(self):
        profile = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        actual = prof_prob("ACG", profile)
        self.assertEqual(1, actual)

    def test_profile_list(self):
        motiflist = ['GGC', 'AAG']
        expected = [[1.0, 0.5, 1.0, 0.5], [
            1.0, 0.5, 1.0, 0.5], [0.5, 1.0, 1.0, 0.5]]
        actual = profile_list(motiflist)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
