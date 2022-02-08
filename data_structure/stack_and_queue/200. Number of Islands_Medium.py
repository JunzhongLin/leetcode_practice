'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    q = [(i, j)]
                    ans += 1

                    while q:
                        ii, jj = q.pop(0)
                        for I, J in (ii + 1, jj), (ii - 1, jj), (ii, jj + 1), (ii, jj - 1):
                            if 0 <= I < m and 0 <= J < n and grid[I][J] == '1':
                                grid[I][J] = '0'
                                q.append((I, J))

