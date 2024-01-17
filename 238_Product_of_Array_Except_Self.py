import numpy as np 
import unittest

def productExceptSelf_cheat(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    product = 1
    #find the product of an array
    for i in range(len(nums)):
        product *= nums[i]

    result = np.full(len(nums),product)
    
    return result/nums

# using prefix posfix        
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res



    

    

class TestProductExceptSelf(unittest.TestCase):

    def test_product_except_self(self):
        # Test case 1
        nums1 = [1, 2, 3, 4]
        self.assertEqual(productExceptSelf(nums1), [24, 12, 8, 6])

        # Test case 2
        nums2 = [5, 2, 3, 1]
        self.assertEqual(productExceptSelf(nums2), [6, 15, 10, 30])

        # Test case 3
        nums3 = [2, 7, 4, 5]
        self.assertEqual(productExceptSelf(nums3), [140, 40, 70, 56])

        # Test case 4
        nums4 = [3, 0, 2, 4]
        self.assertEqual(productExceptSelf(nums4), [0, 24, 0, 0])

        # Test case 5
        nums5 = [1, 1, 1, 1]
        self.assertEqual(productExceptSelf(nums5), [1, 1, 1, 1])

    def test_product_except_self_edge(self):

        # Edge case 1: Empty list
        nums6 = []
        self.assertEqual(productExceptSelf(nums6), [])

        # Edge case 2: List with a single element
        nums7 = [5]
        self.assertEqual(productExceptSelf(nums7), [1])

        # Edge case 3: List with two elements
        nums8 = [2, 3]
        self.assertEqual(productExceptSelf(nums8), [3, 2])

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf_cheat(nums))
    print(productExceptSelf(nums))
    unittest.main()
