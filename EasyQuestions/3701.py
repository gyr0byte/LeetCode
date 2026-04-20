class Solution(object):
    def alternatingSum(self, nums):
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]
        ret = 0
        for i in range(0, len(nums) - 1, 2):
            ret += nums[i] - nums[i+1]
        if len(nums) % 2 == 1:
            ret += nums[-1]
        
        return ret