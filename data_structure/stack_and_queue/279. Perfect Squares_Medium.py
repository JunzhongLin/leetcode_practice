'''
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/solution/
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        que = collections.deque()

        que.append((n, 0))
        visited = set()

        while que:

            remain, depth = que.popleft()
            if remain == 0:
                return depth
            i = 1
            while True:
                new_remain = remain - i ** 2
                i += 1
                if new_remain < 0:
                    break
                if new_remain not in visited:
                    que.append((new_remain, depth + 1))
                    visited.add(new_remain)
