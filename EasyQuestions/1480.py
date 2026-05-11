class Solution(object):
    def runningSum(self, nums):
        sum = []
        sum.append(nums[0])
        for i in range(1, len(nums)):
            sum.append(nums[i] + sum[i-1])
        return sum