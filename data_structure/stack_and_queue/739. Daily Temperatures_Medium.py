'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        stack = [(0, temperatures[0])]

        for i, curr_temp in enumerate(temperatures[1:]):

            while stack and stack[-1][1] < curr_temp:
                ans[stack[-1][0]] = i + 1 - stack[-1][0]
                stack.pop()

            stack.append((i + 1, curr_temp))

        return ans