'''

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''


class Solution:
    def coinChange_td(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def dp(a):
            if a < 0:
                return float('inf')
            elif a == 0:
                return 0
            ans = float('inf')
            for c in coins:
                ans = min(ans, dp(a - c) + 1)

            return ans

        res = dp(amount)

        if res == float('inf'):
            return -1
        else:
            return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                j = i - c
                if j < 0:
                    continue
                else:
                    # print(i, j)
                    dp[i] = min(dp[i], dp[j] + 1)

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]