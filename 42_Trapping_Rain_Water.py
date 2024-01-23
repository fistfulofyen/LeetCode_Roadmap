import unittest

# Take the min of L and R - h[i]
# sample [0,1,0,2,1,0,1,3,2,1,2,1]
# maxL   [0,0,1,1,2,2,2,2,3,3,3,3]
# maxR   [0,0,1,1,2,2,2,2,2,2,1,0]
# trap   [0,0,1,0,1,2,1,0,0,1,0,0]
# ans = sum(trap)
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    if not height: return 0

    l,r = 0, len(height)-1
    l_max, r_max = height[l], height[r]

    ans = 0

    while l < r:
        if l_max < r_max:
            l += 1
            l_max = max(l_max, height[l])
            ans += l_max - height[l]

        else:
            r -= 1
            r_max = max(r_max, height[r])
            ans += r_max - height[r]

    return ans


class TestTrappingRainwater(unittest.TestCase):
    def test_example_case(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        result = trap(height)
        self.assertEqual(result, 6, "Incorrect output for the example case")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
