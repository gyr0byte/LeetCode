class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2   # partition index for nums1
            j = half - i         # partition index for nums2

            # Values just left and right of each partition
            nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i]     if i < m else float('inf')
            nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j]     if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return float(min(nums1_right, nums2_right))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0

            # Adjust binary search bounds
            elif nums1_left > nums2_right:
                hi = i - 1   # move partition left in nums1
            else:
                lo = i + 1   # move partition right in nums1

        return 0.0