class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        return self.subsets(nums[1:]) + [([nums[0]] + s) for s in self.subsets(nums[1:])]
