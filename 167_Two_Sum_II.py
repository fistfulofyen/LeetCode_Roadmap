import unittest

def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target and i !=j:
                return [i+1,j+1]
            
def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    l, r = 0, len(numbers) -1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum > target:
            r -=1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]
        
    return []




class TestTwoSum(unittest.TestCase):

    def test_example_case(self):
        numbers = [2, 7, 11, 15]
        target = 9
        result = two_sum(numbers, target)
        self.assertEqual(result, [1, 2])

    def test_another_case(self):
        numbers = [3, 24, 50, 79, 88, 150, 345]
        target = 200
        result = two_sum(numbers, target)
        self.assertEqual(result, [3, 6])

    def test_single_solution(self):
        numbers = [1, 2, 3, 4, 5]
        target = 9
        result = two_sum(numbers, target)
        self.assertEqual(result, [4, 5])

if __name__ == '__main__':
    unittest.main()