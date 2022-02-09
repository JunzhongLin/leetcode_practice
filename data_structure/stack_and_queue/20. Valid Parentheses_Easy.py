class Solution:
    def isValid(self, s: str) -> bool:

        pare_stack = []
        pare_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for cha in s:
            if cha in ('(', '[', '{'):
                pare_stack.append(cha)

            elif cha in (')', ']', '}'):
                if pare_stack == []:
                    return False

                if cha != pare_dict[pare_stack.pop()]:
                    return False

        if pare_stack == []:
            return True

        return False