'''

Write a Python program to solve the Fibonacci sequence using recursion.
'''

class Solution:

    def fibonacci(self, n):
        if n==1:
            return 0
        elif n==2:
            return 1

        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)


if __name__ == '__main__':
    res = Solution().fibonacci(7)