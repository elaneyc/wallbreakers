class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)

        if row == 0: return 0

        col = len(grid[0])

        self.islands = sum([int(grid[i][j]) for i in range(row) for j in range(col) if grid[i][j] == '1'])
        parent = [i for i in range(row*col)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            x_root = find(x)
            y_root = find(y)

            if x_root == y_root: return

            self.islands -= 1
            parent[x_root] = y_root



        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)

        return self.islands
