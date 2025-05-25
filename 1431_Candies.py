import unittest
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_candies = [extraCandies + num for num in candies]
        
        result = []
        for i in range(len(candies)):
            is_greatest = True
            for j in range(len(candies)):
                if new_candies[i]  < candies[j]:
                    is_greatest = False
                    break
            result.append(is_greatest)
            

        return result




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])

    def test_all_same_candies(self):
        self.assertEqual(self.solution.kidsWithCandies([4, 4, 4, 4], 1), [True, True, True, True])

    def test_minimal_case(self):
        self.assertEqual(self.solution.kidsWithCandies([1], 0), [True])

    def test_no_extra_candies(self):
        self.assertEqual(self.solution.kidsWithCandies([1, 2, 3], 0), [False, False, True])

    def test_large_extra_candies(self):
        self.assertEqual(self.solution.kidsWithCandies([1, 2, 3], 10), [True, True, True])

if __name__ == '__main__' :
    unittest.main()