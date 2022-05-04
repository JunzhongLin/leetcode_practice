'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = prices[0], prices[0]

        for price in prices[1:]:
            if price <= buy:
                buy = price
            elif price > buy:
                sell = price
                profit = max(sell - buy, profit)

        return profit
