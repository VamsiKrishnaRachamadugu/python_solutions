import unittest
import add


class test_sample(unittest.TestCase):

    # positive testcase
    def test_add(self):
        self.assertEqual(add.obj_add.addition(2, 6), 8)

    # negative testcase -uncomment it and run for both
    # def test_add1(self):
    #     self.assertNotEqual(add.obj_add.addition(2, 2), 5)


if __name__ == '__main__':
    unittest.main()
