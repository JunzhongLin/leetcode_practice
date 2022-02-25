'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.full = set('123456789')
        self.board = board
        self.emptys = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    self.emptys.append((i, j))
                else:
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[i // 3 * 3 + j // 3].add(num)

        self.max_counts = len(self.emptys)
        self.found_solution = False
        if self.max_counts == 0:
            return

        self._backtrack_sudoku(0)

    def _backtrack_sudoku(self, count):
        if count >= self.max_counts:
            self.found_solution = True
            return None  # finished inputing
        i, j = self.emptys[count]
        p_vals = self._possible_vals(i, j)
        for val in p_vals:
            self._enter_num(i, j, val)
            self._backtrack_sudoku(count + 1)
            if self.found_solution:
                return None
            self._remove_num(i, j, val)

    def _possible_vals(self, i, j):
        p_vals_set = self.full - (self.rows[i] | self.cols[j] | self.boxes[i // 3 * 3 + j // 3])
        return list(p_vals_set)

    def _enter_num(self, i, j, val):
        self.board[i][j] = val
        self.rows[i].add(val)
        self.cols[j].add(val)
        self.boxes[i // 3 * 3 + j // 3].add(val)

    def _remove_num(self, i, j, val):
        self.board[i][j] = '.'
        self.rows[i].remove(val)
        self.cols[j].remove(val)
        self.boxes[i // 3 * 3 + j // 3].remove(val)