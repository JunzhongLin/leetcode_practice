'''

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''


class Solution:
    # time : O(numRows **2)
    # space: O(numRows **2)
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for _ in range(numRows - 2):
            temp = [1] + [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)] + [1]
            res.append(temp)

        return res
