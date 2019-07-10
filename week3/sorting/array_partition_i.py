class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums) / 2

        pair_mins = []

        for i in range(0, len(nums) - 1, 2):
            pair_mins.append(min(nums[i], nums[i+1]))

        return sum(pair_mins)
