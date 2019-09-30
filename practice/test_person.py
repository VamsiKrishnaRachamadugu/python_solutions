import unittest
import Person


class Test(unittest.TestCase):
    def test_0_setname(self):
        print('Start setname test')

        Person.p.set_name('Krishna', 13)

    def test_1_getname(self):
        print('Starting getname test')
        name = Person.p.get_name()
        print(name)
        self.assertEqual(self.get_name(), (13, 'Krishna'))


if __name__ == '__main__':
    unittest.main()
