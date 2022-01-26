'''

Write a Python program to calculate the sum of
the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

sum_series(6) -> 12
sum_series(10) -> 30
'''


class Solution:

    def sum_digits(self, num):
        if num-2 < 0:
            return 0
        else:
            return num + self.sum_digits(num-2)

if __name__ == '__main__':
    res = Solution().sum_digits(8)
