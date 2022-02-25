mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
tar = 0


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False

        n, m = len(matrix), len(matrix[0])
        # print(n, m)

        found = False

        pivot_col = m // 2
        for i in range(n):
            print(i, pivot_col, matrix)
            if matrix[i][pivot_col] == target:
                found = True
                return found
            elif matrix[i][pivot_col] > target:
                break
        # print(i, pivot_col)
        if matrix[i][pivot_col] < target:
            i += 1

        found = self.searchMatrix([row[pivot_col + 1:] for row in matrix[:i]], target)
        if not found:
            found = self.searchMatrix([row[:pivot_col] for row in matrix[i:]], target)

        return found

s = Solution().searchMatrix(mat, tar)