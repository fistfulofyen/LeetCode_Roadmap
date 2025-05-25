from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = []
        for num in nums:
            if num != 0:
                non_zero.append(num)
        
        number_of_non_zero_num = len(non_zero)

        for i in range(len(nums)):
            if i <= number_of_non_zero_num -1 :
                nums[i] = non_zero[i]
            else:
                nums[i] = 0
        
        return nums
    
nums = [0]
sol = Solution()
print(sol.moveZeroes(nums))


