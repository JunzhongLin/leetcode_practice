'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        parse_cha = True
        parse_int = True
        digits = list('0123456789')
        for cha in s:
            stack.append(cha)
            if cha == ']':
                vals = []
                temp_list = []
                while parse_cha:
                    if stack[-1] in digits:
                        break
                    temp_list.append(stack.pop())
                while parse_int:
                    vals.append(stack.pop())
                    if stack == [] or stack[-1] not in digits:
                        break
                vals.reverse()
                val = int(''.join(vals))
                temp_list.reverse()
                stack.append(''.join(temp_list[1:-1] * val))

        return ''.join(stack)
