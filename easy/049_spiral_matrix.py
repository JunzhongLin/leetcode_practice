'''

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n**2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
'''


class Solution:

    def make_spiral_matrix(self, num):
        # (0,0) (0,1) (0,2) (0,3) (1,3) (2,3) (3,3) (3,2) (3,1) (3,0) (2,0), (1,0) (1, 1)
        # (1,2) (2,2) (2,1)
        res = [[-1] * num for _ in range(num)]
        up, left, down, right = 0, 0, num-1, num-1
        val = 1
        while up < down and left < right:
            for i in range(left, right):
                res[up][i] = val
                val += 1
            for i in range(up, down):
                res[i][right] = val
                val += 1
            for i in range(right, left, -1):
                res[down][i] = val
                val += 1
            for i in range(down, up, -1):
                res[i][left] = val
                val += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        if num % 2 ==1:
            res[num//2][num//2] = val

        return res


if __name__ == '__main__':
    res = Solution().make_spiral_matrix(3)