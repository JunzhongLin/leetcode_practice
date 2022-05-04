'''

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        c_start, c_end = 0, n-1
        for r in range(n//2):
            for i in range(c_start, c_end):
                matrix[r][i], matrix[i][n-r-1], matrix[n-r-1][n-i-1], matrix[n-i-1][r] =\
                    matrix[n-i-1][r], matrix[r][i], matrix[i][n-r-1], matrix[n-r-1][n-i-1]
            c_start += 1
            c_end -= 1