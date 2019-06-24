class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solutions = {}
        for i in range(len(nums)):
            if nums[i] in solutions:
                return [solutions[nums[i]], i]
            else:
                solutions[target - nums[i]] = i
