'''

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        digits_set = set(list('0123456789'))
        add_sub = set(list('-+'))
        mul_div = set(list('*/'))
        n = len(s)
        num = ''
        i = 0
        res = 0
        while i < n:
            l = s[i]

            if l == ' ':
                i += 1
                continue
            elif l in digits_set:
                num += l
                if i + 1 == n or s[i + 1] in add_sub or s[i + 1] in mul_div or s[i + 1] == ' ':
                    stack.append(int(num))
                    num = ''
            elif l in add_sub:
                num += l
            elif l in mul_div:
                num_a = stack.pop()
                num_b = ''
                while i + 1 < n and s[i + 1] not in add_sub and s[i + 1] not in mul_div:
                    num_b += s[i + 1]
                    i += 1
                num_b = int(num_b)
                if l == '*':
                    stack.append(num_a * num_b)
                else:
                    stack.append(abs(num_a) // num_b * (-1) if num_a < 0 else num_a // num_b)
            i += 1

        while stack:
            res += stack.pop()

        return res