import unittest

def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums [r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res



    
class TestThreeSum(unittest.TestCase):
    
    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = three_sum(nums)
        expected_result = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(result), sorted(expected_result))

    def test_example_2(self):
        nums = [0, 1, 1]
        result = three_sum(nums)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_example_3(self):
        nums = [0, 0, 0]
        result = three_sum(nums)
        expected_result = [[0, 0, 0]]
        self.assertEqual(sorted(result), sorted(expected_result))

    def test_custom_example(self):
        nums = [-1, 2, 0, -1, 1, -2]
        result = three_sum(nums)
        expected_result = [[-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(result), sorted(expected_result))

    def test_empty_array(self):
        nums = []
        result = three_sum(nums)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_no_triplets(self):
        nums = [1, 2, 3]
        result = three_sum(nums)
        expected_result = []
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
