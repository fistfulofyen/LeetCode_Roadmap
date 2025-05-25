from typing import List
    
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')  # First smallest element
        second = float('inf')  # Second smallest element

        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  # Update the second smallest number
            else:
                # If num is greater than both first and second, we found a triplet
                return True

        return False


nums = [20,100,10,12,5,13]
sol = Solution()
print(sol.increasingTriplet(nums))