import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort import merge_sort
import random


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-3, -1, -4, -2]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(merge_sort([3, -1, 0, -2, 5]), [-2, -1, 0, 3, 5])

    def test_reverse_sort(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5], reverse=True), [5, 4, 3, 1, 1])

    def test_random_lists(self):
        for _ in range(100):
            arr = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            sorted_arr = merge_sort(arr)
            self.assertEqual(sorted_arr, sorted(arr))

    def test_random_lists_reverse(self):
        for _ in range(100):
            arr = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            sorted_arr = merge_sort(arr, reverse=True)
            self.assertEqual(sorted_arr, sorted(arr, reverse=True))


if __name__ == '__main__':
    unittest.main()
