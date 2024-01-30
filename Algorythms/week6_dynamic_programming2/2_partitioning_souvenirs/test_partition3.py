from unittest import TestCase
from partition3 import check_possibilities

class Test(TestCase):
    def test_check_possibilities(self):
        self.assertEqual(check_possibilities([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 36), True)

    def test_check_possibilities2(self):
        self.assertEqual(check_possibilities([30], 10), False)

    def test_check_possibilities3(self):
        self.assertEqual(check_possibilities([], 0), False)

    def test_check_possibilities4(self):
        self.assertEqual(check_possibilities([3,3,3,3], 4), False)

    def test_check_possibilities5(self):
        self.assertEqual(check_possibilities([1,1,1], 1), True)

    def test_check_possibilities6(self):
        self.assertEqual(check_possibilities([1,2,3,4,5,6], 7), True)

    def test_check_possibilities6(self):
        self.assertEqual(check_possibilities([1,2,3,4,5,6,7,8], 12), True)

    # def test_check_possibilities7(self):
    #     self.assertEqual(check_possibilities([1,2,3,4,5,6,7,9], 12), False)