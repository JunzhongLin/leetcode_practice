class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        que = []
        for j in (0, n - 1):
            for i in range(m):
                if board[i][j] == 'O':
                    que.append((i, j))

        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == 'O':
                    que.append((i, j))

        visited = set(que)

        while que:
            (i, j) = que.pop(0)
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'O' and (ii, jj) not in visited:
                    que.append((ii, jj))
                    visited.add((ii, jj))

        # print(visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'

        return board