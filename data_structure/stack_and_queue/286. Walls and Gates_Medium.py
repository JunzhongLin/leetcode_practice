'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(rooms[i]) if not r]
        while q:
            i, j = q.pop(0)
            for (I, J) in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                if 0 <= I < m and 0 <= J < n and rooms[I][J] > 2 ** 30:
                    rooms[I][J] = rooms[i][j] + 1
                    q.append((I, J))

