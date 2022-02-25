'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

'''

from collections import defaultdict


class Solution(object):
    def __init__(self, ):
        self.attack_pos = defaultdict(int)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.backtrack_nqueen(n, 0, 0)

    def is_not_under_attack(self, r, c):
        if self.attack_pos[r, c] >= 1:
            return False
        return True

    def place_queen(self, n, r, c):
        dif_rc = r - c
        sum_rc = r + c
        for i in range(n):
            self.attack_pos[i, c] += 1
            self.attack_pos[r, i] += 1
            if 0 <= sum_rc - i < n:
                self.attack_pos[i, sum_rc - i] += 1
            if 0 <= i - dif_rc < n:
                self.attack_pos[i, i - dif_rc] += 1

    def remove_queen(self, n, r, c):
        dif_rc = r - c
        sum_rc = r + c
        for i in range(n):
            self.attack_pos[i, c] -= 1
            self.attack_pos[r, i] -= 1
            if 0 <= sum_rc - i < n:
                self.attack_pos[i, sum_rc - i] -= 1
            if 0 <= i - dif_rc < n:
                self.attack_pos[i, i - dif_rc] -= 1

    def backtrack_nqueen(self, n, row=0, count=0):
        for col in range(n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(n, row, col)
                if row + 1 == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                else:
                    # we move on to the next row
                    count = self.backtrack_nqueen(n, row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(n, row, col)
        return count


test = Solution()
test.place_queen(5, 2, 1)
