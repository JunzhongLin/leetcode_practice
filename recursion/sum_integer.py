'''
Write a Python program to get the sum of a non-negative integer.
'''


class Solution:
    def __init__(self, num):
        self.num = num

    def sum_digits(self, x):
        if x == 1:
            return int(str(self.num)[-1])
        else:
            return int(str(self.num)[-x]) + self.sum_digits(x-1)


def sumDigits(n):
    if n == 0:
      return 0
    else:
      return n % 10 + sumDigits(int(n / 10))

print(sumDigits(345))
print(sumDigits(45))

if __name__ == '__main__':
    res = Solution(12348).sum_digits(5)