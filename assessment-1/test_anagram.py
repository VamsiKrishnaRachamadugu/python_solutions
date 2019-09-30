import unittest
from anagram import is_anagaram


class test_anagram(unittest.TestCase):
    def test_angram(self):
        self.assertEqual(is_anagaram('anagram', 'nagaram'), True)


if __name__ == '__main__':
    unittest.main()
