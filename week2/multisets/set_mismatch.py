class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()

        result = []
        for i in range(len(nums)-1):
            # Find num that appears twice
            if nums[i] == nums[i+1]:
                result.insert(0,nums[i])

            if nums[i] == nums[i+1]-2:
                # Case when missing num is internal
                result.append((nums[i]+nums[i+1])/2)


        if len(result) == 1:
            # Case if missing number is at the end or the beginning
            if nums[-1] != len(nums):
                result.append(len(nums))
            elif nums[0] != 1:
                result.append(1)

        return result
