'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:

        def helper(num):
            if num == 1 or num == 0:
                return 1
            elif num in self.cache:
                return self.cache[num]

            steps = helper(num - 1) + helper(num - 2)
            self.cache[num] = steps

            return steps

        return helper(n)
