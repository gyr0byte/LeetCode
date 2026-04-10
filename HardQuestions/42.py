class Solution:
    def trap(self, height: list[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_left = max_right = 0
        water = 0

        while lo < hi:
            if height[lo] <= height[hi]:
                if height[lo] >= max_left:
                    max_left = height[lo]       # new left boundary
                else:
                    water += max_left - height[lo]  # trapped between walls
                lo += 1
            else:
                if height[hi] >= max_right:
                    max_right = height[hi]      # new right boundary
                else:
                    water += max_right - height[hi] # trapped between walls
                hi -= 1

        return water