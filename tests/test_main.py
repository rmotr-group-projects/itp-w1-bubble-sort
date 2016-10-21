import unittest

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(bubble_sort([]) , [])

    def test_one_element(self):
        self.assertEqual(bubble_sort([1]) , [1])

    def test_two_elements(self):
        self.assertEqual(bubble_sort([2, 1]) , [1, 2])

    def test_multiple_elements(self):
        self.assertEqual(bubble_sort([1, 3, 2, 6, 5]), [1, 2, 3, 5, 6])