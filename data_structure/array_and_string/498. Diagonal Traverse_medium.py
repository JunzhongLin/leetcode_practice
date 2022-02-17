'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        res = []
        start_points = []
        end_points = []
        for i_s in range(len(mat)):
            start_points.append((i_s + 1, 0))
        for j_s in range(len(mat[0]) - 1):
            start_points.append((i_s + 1, j_s + 1))

        for j_e in range(len(mat[0])):
            end_points.append((0, j_e + 1))
        for i_e in range(len(mat) - 1):
            end_points.append((i_e + 1, j_e + 1))

        for (i_s, j_s), (i_e, j_e) in zip(start_points, end_points):
            temp = []
            ii, jj = i_s, j_s
            # print(i_e, j_e)
            while (ii, jj) != (i_e, j_e):
                # print(ii, jj)
                temp.append(mat[ii - 1][jj])
                ii -= 1
                jj += 1

            if (i_s + j_s) % 2 == 0:
                temp.reverse()

            res.extend(temp)

        return res
