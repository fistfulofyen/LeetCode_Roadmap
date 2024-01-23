import unittest

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    ans = 0

    for l in range(len(height)):
        for r in range(l+1,len(height)):
            area = (r - l) * min(height[l],height[r])
            ans = max(ans,area)

    return ans

def max_water_container(height):
    """
    Finds the maximum amount of water a container can store.

    Parameters:
    - height (List[int]): The height of the vertical lines.

    Returns:
    - int: Maximum amount of water the container can store.
    """
    n = len(height)
    max_water = 0
    left, right = 0, n - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


class TestMaxWaterContainer(unittest.TestCase):
    def test_max_water_container(self):
        # Test case 1
        self.assertEqual(max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

        # Test case 2
        self.assertEqual(max_water_container([1, 1]), 1)

        # Test case 3
        self.assertEqual(max_water_container([4, 3, 2, 1, 4]), 16)

        # Test case 4
        self.assertEqual(max_water_container([1, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()