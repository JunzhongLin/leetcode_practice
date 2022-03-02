'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n // 2)
            if n % 2 == 0:
                return half * half
            if n % 2 != 0:
                return half * half * x

        if n < 0:
            x, n = 1 / x, -n

        return helper(x, n)