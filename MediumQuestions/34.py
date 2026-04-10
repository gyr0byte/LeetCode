class Solution:
    def searchRange(self, nums, target):
        return [self.first_position(nums, target), self.last_position(nums, target)]

    def first_position(self, nums, target):
        low, high = 0, len(nums) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return result

    def last_position(self, nums, target):
        low, high = 0, len(nums) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result