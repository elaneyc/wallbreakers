class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []

        
        for i in range(len(A)):
            for j in range(len(A[i])):
                try:
                    transpose[j]
                except:
                    transpose.append([])
                transpose[j].append(A[i][j])

        return transpose
