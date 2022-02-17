'''
Given two binary strings a and b, return their sum as a binary string.
'''


class Solution:
    # time: O(max(len(a), len(b)))
    # space: O(max(len(a), len(b)))
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        plus = 0
        for i in range(1, max(len(a) + 1, len(b) + 1)):
            digit_a = int(a[-i]) if i <= len(a) else 0
            digit_b = int(b[-i]) if i <= len(b) else 0
            add_on = digit_a + digit_b + plus
            digit = add_on % 2
            plus = add_on // 2

            res = str(digit) + res
        if plus > 0:
            res = '1' + res
        return res