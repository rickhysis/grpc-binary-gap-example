import unittest
from binary_gap import count_gap

class TestBinaryGap(unittest.TestCase):

    def test_count_gap(self):
        self.assertEqual(count_gap(529), 4, "Should be 4")

    def test_count_gap_character(self):
        with self.assertRaises(Exception): count_gap('529')

if __name__ == '__main__':
    unittest.main()