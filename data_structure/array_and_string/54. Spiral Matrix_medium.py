'''
Given an m x n matrix, return all elements of the matrix in spiral order.

'''


class Solution:
    # time: O(n)
    # space: O(2n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        visited = set()
        res = []
        travel = True
        start_point = (0, -1)
        m, n = len(matrix), len(matrix[0])

        while True:
            i, j = start_point
            direction = (0, 0)

            for ii, jj in (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j):
                if (ii, jj) not in visited and 0 <= ii < m and 0 <= jj < n:
                    direction = (ii - i, jj - j)
                    travel = True
                    break
                else:
                    travel = False

            if not travel:
                return res

            while 0 <= i + direction[0] < m and 0 <= j + direction[1] < n and (
            i + direction[0], j + direction[1]) not in visited:
                i += direction[0]
                j += direction[1]
                res.append(matrix[i][j])
                visited.add((i, j))

            start_point = (i, j)

