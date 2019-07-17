class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for num in nums1:
            for i in range(len(nums2)-1, -1, -1):
                if nums2[i] != num:
                    stack.append(nums2[i])
                else:
                    break

            found = False
            while len(stack) > 0:
                temp = stack.pop()
                if temp > num:
                    result.append(temp)
                    found = True
                    stack = []

            if not found:
                result.append(-1)

        return result
