from typing import List

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         three_zeros = 0
#         i = 0
#         while i < len(flowerbed) - 2:
#         # Check for three consecutive zeros
#             if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
#                 three_zeros += 1
#                 i += 2  # Skip the next two indices (total of 3)
#             else:
#                 i += 1
        
#         return n <= three_zeros
    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        empty_spot = 0
        
        while i < len(flowerbed):
            # Check for an empty spot
            if flowerbed[i] == 0:
                # Check if we can place a flower at position i
                # If we're at the first position, just check the next one
                if (i == 0 and (i + 1 < len(flowerbed) and flowerbed[i + 1] == 0)) or \
                   (i == len(flowerbed) - 1 and (i - 1 >= 0 and flowerbed[i - 1] == 0)) or \
                   (i > 0 and i < len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0) or \
                    (i == 0 and len(flowerbed) - 1 == 0):
                    flowerbed[i] = 1  # Place a flower
                    empty_spot += 1
                    i += 2  # Skip the next spot (because flowers can't be adjacent)
                    if empty_spot >= n:  # If we have placed enough flowers, return True
                        return True
                else:
                    i += 1  # If we can't place a flower, move to the next spot
            else:
                i += 1  # Move to the next spot if the current spot is occupied

        return empty_spot >= n


                    

                

    

solution = Solution()

print(solution.canPlaceFlowers([0,0,0,0,0,1],3))