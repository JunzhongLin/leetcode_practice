"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:

    def valid_parentheses(self, strings):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for x in strings:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack)!=0:
                    top_element = stack.pop()
                    if x != top_element:
                        return False
                    else:
                        continue
                else:
                    return False

        return len(stack) == 0


class Solution_stack:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False


if __name__ == '__main__':
    sol = Solution()
    res = sol.valid_parentheses('([{}])')