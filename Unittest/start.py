from .calculator import Count
import unittest


class TestCount(unittest.TestCase):

    def setUp(self) -> None:
        print('test start')

    def testadd(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def tearDown(self) -> None:
        print('test end')


if __name__=='__main__':
    unittest.main()