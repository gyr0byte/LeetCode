class Solution(object):
    def pivotArray(self, nums, pivot):
        less, equal, greater = [], [], []
        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                less.append(num)
        less.extend(equal)
        less.extend(greater)
        return less