class Solution:
    def maximalSquare(self, matrix) -> int:
        ans = 0

        m, n = len(matrix), len(matrix[0])
        stack = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    stack.append((i, j))

        stack.sort(key=lambda x: -min(m-x[0], n-x[1]))
        print(stack)

        while stack:
            i, j = stack.pop(0)
            print('i:', i, 'j:', j, 'ans:', ans)

            if stack and ans > (min(m-i, n-j)) ** 2:
                break

            length = 1
            delta = 1
            while i + delta < m and j + delta < n:
                found_zero = False

                for ii in range(i, i + delta + 1):
                    if matrix[ii][j + delta] == '0':
                        found_zero = True
                for jj in range(j, j + delta + 1):
                    if matrix[i + delta][jj] == '0':
                        found_zero = True
                if found_zero:
                    break
                else:
                    delta += 1
                    length += 1

            ans = max(length ** 2, ans)

        return ans

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # print(i, j)
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    max_len = max(max_len, dp[i + 1][j + 1])

        return max_len * max_len

b=[["0","0","0","0","1","1","1","0","1"],
   ["0","0","1","1","1","1","1","0","1"],
   ["0","0","0","1","1","1","1","1","0"]]

res = Solution().maximalSquare(b)
