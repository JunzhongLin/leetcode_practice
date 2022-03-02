'''

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''


class Solution:
    def __init__(self, ):
        self.cache = {}
        self.cache[0] = [1]
        self.cache[1] = [1, 1]

    def getRow(self, rowIndex: int) -> List[int]:

        row_key = 2
        for _ in range(rowIndex - 1):
            if row_key not in self.cache:
                nums = self.cache[row_key - 1]
                self.cache[row_key] = [1] + [nums[i] + nums[i + 1] for i in range(row_key - 1)] + [1]
            row_key += 1

        return self.cache[rowIndex]
