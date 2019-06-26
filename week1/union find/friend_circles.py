class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        seen = set()

        def dfs(n):
            for nbr, adj in enumerate(M[n]):
                if adj == 1 and nbr not in seen:
                    seen.add(nbr)
                    dfs(nbr)

        circles = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                circles += 1
        return circles



        
