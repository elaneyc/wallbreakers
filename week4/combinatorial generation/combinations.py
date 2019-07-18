class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n+1)]
        return self.list_combinations(nums, k)

    def list_combinations(self,A, k):
        if k == 0:
            return [[]]
        if len(A) == k:
            return [list(A)]
        result = [[A[0]] + c for c in self.list_combinations(A[1:], k - 1)]
        result += self.list_combinations(A[1:], k)
        return result
