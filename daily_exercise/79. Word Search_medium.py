'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []
        m = len(board)
        n = len(board[0])
        # visited = set()

        if len(word) > m * n:
            return False

        l = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    stack.append(((i, j), 0, visited))
                    visited.add((i, j))

        while stack:
            (i, j), k, visited = stack.pop()
            if k == len(word) - 1:
                return True
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == word[k + 1] and (ii, jj) not in visited:
                    # print(ii, jj, l)
                    visited_new = visited.copy()
                    stack.append(((ii, jj), k + 1, visited_new))
                    visited_new.add((ii, jj))
                    if k + 1 == len(word) - 1:
                        return True

        return False