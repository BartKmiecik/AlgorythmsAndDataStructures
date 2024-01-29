from unittest import TestCase
from knapsack import max_gold

class Test(TestCase):
    def test_simple(self):
        self.assertEqual(max_gold(capacity=10, weights=[1, 4, 8]), 9)

    def test_capa_smoler(self):
        self.assertEqual(max_gold(capacity=1, weights=[2, 4, 8]), 0)

    def test_capa_bigger(self):
        self.assertEqual(max_gold(capacity=15, weights=[2, 4, 8]), 14)

    def test_three(self):
        self.assertEqual(max_gold(capacity=5, weights=[1, 1, 1]), 3)
