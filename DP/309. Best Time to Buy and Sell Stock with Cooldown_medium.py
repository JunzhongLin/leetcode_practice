class Solution:
    def maxProfit_td(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(maxsize=None)
        def dp(i, holding):
            if i >= n:
                return 0

            do_nothing = dp(i + 1, holding)

            if holding:
                do_something = prices[i] + dp(i + 2, 0)
            else:
                do_something = -prices[i] + dp(i + 1, 1)

            return max(do_something, do_nothing)

        profits = dp(0, 0)

        return profits

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for holding in range(2):

                do_nothing = dp[i + 1][holding]

                if holding:
                    do_something = dp[i + 2][0] + prices[i]
                else:
                    do_something = dp[i + 1][1] - prices[i]

                dp[i][holding] = max(do_something, do_nothing)

        return dp[0][0]