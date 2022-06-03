class Solution:
    def isToeplitzMatrix_recur(self, matrix: List[List[int]]) -> bool:

        def helper(sub_matrix):
            if len(sub_matrix) == 1 or len(sub_matrix[0]) == 1:
                return True

            m, n = len(sub_matrix), len(sub_matrix[0])

            if helper([row[:-1] for row in sub_matrix[:-1]]):
                for i in range(1, n):
                    if sub_matrix[m - 1][i] != sub_matrix[m - 2][i - 1]:
                        return False
                for j in range(1, m):
                    if sub_matrix[j][n - 1] != sub_matrix[j - 1][n - 2]:
                        return False
                return True

            return False

        return helper(matrix)

    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True