from functools import lru_cache

class SolutionWrong:
    def numWays(self, n: int, k: int) -> int:

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == 0:
                return 1
            if i == 1:
                return k

            res = 0
            for jj in range(k):
                if jj != j:
                    res += dp(i - 1, jj)
                else:
                    res += dp(i - 1, jj) - dp(i - 2, jj)
            return res

        ans = 0
        for jj in range(k):
            ans += dp(n - 1, jj)
        return ans


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        return total_ways(n)

a = Solution()