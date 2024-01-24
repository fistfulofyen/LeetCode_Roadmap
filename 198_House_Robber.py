import unittest

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Initialize an array to store the maximum amount of money robbed at each house
    dp = [0] * len(nums)
    
    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Dynamic programming to calculate the maximum amount of money robbed at each house
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

class TestRobbery(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)

    def test_example2(self):
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

    def test_empty_input(self):
        self.assertEqual(rob([]), 0)

    def test_single_house(self):
        self.assertEqual(rob([5]), 5)

    def test_multiple_houses(self):
        self.assertEqual(rob([6, 3, 10, 8, 2, 7]), 23)

if __name__ == '__main__':
    unittest.main()

