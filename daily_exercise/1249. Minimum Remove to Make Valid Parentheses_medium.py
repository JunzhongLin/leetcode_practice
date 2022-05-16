class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        list_s = list(s)
        for i, cha in enumerate(list_s):
            if cha == '(' or cha == ')':
                # if not stack or stack[-1][1]==')':
                #     stack.append((i, cha))
                if stack != [] and list_s[stack[-1]] == '(' and cha == ')':
                    stack.pop()
                else:
                    stack.append(i)

        res = ''
        for j in range(len(s)):
            if j in stack:
                continue
            res += list_s[j]

        return res