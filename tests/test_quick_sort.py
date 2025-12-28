import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quick_sort import quick_sort
import random


class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(quick_sort([-3, -1, -4, -2]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(quick_sort([3, -1, 0, -2, 5]), [-2, -1, 0, 3, 5])

    def test_reverse_sort(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5], reverse=True), [5, 4, 3, 1, 1])

    def test_random_lists(self):
        for _ in range(100):
            arr = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            sorted_arr = quick_sort(arr)
            self.assertEqual(sorted_arr, sorted(arr))

    def test_random_lists_reverse(self):
        for _ in range(100):
            arr = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            sorted_arr = quick_sort(arr, reverse=True)
            self.assertEqual(sorted_arr, sorted(arr, reverse=True))

    def test_large_list(self):
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, sorted(arr))


if __name__ == '__main__':
    unittest.main()
