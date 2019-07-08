class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        highest = 0
        index = 0
        descending = False
        for i in range(len(A)):
            n = A[i]
            # Will only reach here if stopped ascending
            if descending:
                break
            if n > highest:
                index = i
                highest = n
            elif n < highest:
                descending = True
        return index
