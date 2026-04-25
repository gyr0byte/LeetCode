class Solution(object):
    def pivotArray(self, nums, pivot):
        less, equal, greater = [], [], []
        for i in range(len(nums)):
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            else:
                less.append(nums[i])
        return less + equal + greater