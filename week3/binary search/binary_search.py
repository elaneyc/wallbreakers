class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums) / 2
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[mid] < target:
                start = mid + 1
                mid = (start + end) / 2
            elif nums[mid] > target:
                end = mid - 1
                mid = (start + end) / 2
            else:
                return mid
        # Number not in nums if get here
        return -1
