class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # With binary search
        mid = len(A) / 2
        start = 0
        end = len(A)-1

        while start < end:
            mid = (start + end) / 2
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] > A[mid]:
                end = mid
            else:
                start = mid + 1

        return -1
