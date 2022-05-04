class Solution:
    def uniquePaths_td(self, m: int, n: int) -> int:

        @lru_cache(maxsize=None)
        def dp(r, c):

            if r == 0:
                return 1
            elif c == 0:
                return 1

            return dp(r - 1, c) + dp(r, c - 1)

        return dp(m - 1, n - 1)

    def uniquePaths(self, m: int, n: int) -> int:

        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]