class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        '''

        :param deadends:
        :param target:
        :return:
        Time Complexity: O(N^2 * A^N + D)
        where, N is Number of dials (4 in our case)
        A is number of alphabets (10 in our case -> 0 to 9)
        D is the size of deadends.
        
        There are 10 x 10 x 10 x 10 possible combinations => 10^4 => A^N
        For each combination, we are looping 4 times (which is N) and in each iteration, there are substring operations ( which is O(N) * constant) => O(4N*constant) => O(4N) => O(NN) => O(N^2)
        Total complexity => A^N * N^2, plus D to create the hashset => N^2 * A^N + D
        '''
        q = [('0000', 0)]
        seen = set()
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        def _neighbors(node, seen, deadends):
            val, depth = [n for n in node[0]], node[1]
            for i in range(4):
                for j in (1, -1):
                    new_val = val[:]
                    new_val[i] = str((int(new_val[i]) + j + 10) % 10)
                    new_node = (''.join(new_val), depth + 1)
                    if new_node[0] not in seen and new_node[0] not in deadends:
                        yield new_node

        while q:
            node = q.pop(0)
            for new_node in _neighbors(node, seen, deadends):
                if new_node[0] == target:
                    return new_node[1]
                q.append(new_node)
                seen.add(new_node[0])

        return -1

res = Solution().openLock([], '8888')