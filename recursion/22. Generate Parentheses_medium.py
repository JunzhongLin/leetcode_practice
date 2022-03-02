'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sub_res = [], []

        def helper(n):
            if n == 1:
                return ['()']
            res = set()
            for p in helper(n - 1):
                res.add('(' + p + ')')
                res.add(p + '()')
                res.add('()' + p)

            return list(res)

        def backtracking(l, r, sub_res):
            if l == r and l == n:
                res.append(''.join(sub_res))
                return None

            if l < n:
                sub_res.append('(')
                backtracking(l + 1, r, sub_res)
                sub_res.pop()

            if r < l:
                sub_res.append(')')
                backtracking(l, r + 1, sub_res)
                sub_res.pop()

        backtracking(0, 0, [])
        return res