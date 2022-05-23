class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # time: O(n)
        # space: O(n)
        # n = len(str)
        res = 0
        stack = []

        for i in list(s):
            if i not in ['(', ')']:
                continue
            else:
                if i == ')' and len(stack) == 0:
                    res += 1
                elif i == '(':
                    stack.append(i)
                else:
                    stack.pop()

        res += len(stack)

        return res