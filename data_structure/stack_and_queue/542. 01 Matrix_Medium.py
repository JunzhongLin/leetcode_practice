'''

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''


class Solution:
    def updateMatrix(self, mat):

        if mat == []:
            return []

        visited = set()
        queue = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        print(queue)

        while queue:
            i, j = queue.pop(0)
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited:
                    mat[ii][jj] = mat[i][j] + 1
                    queue.append((ii, jj))
                    visited.add((ii, jj))

        return mat

mat = [[0,0,0],[0,1,0],[1,1,1]]
res = Solution().updateMatrix(mat)
