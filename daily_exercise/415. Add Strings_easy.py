class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        add_on = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i != -1 or j != -1:
            if i != -1 and j != -1:
                digit_sum = int(num1[i]) + int(num2[j]) + add_on
                i -= 1
                j -= 1
            elif i != -1 and j == -1:
                digit_sum = int(num1[i]) + add_on
                i -= 1
            else:
                digit_sum = int(num2[j]) + add_on
                j -= 1

            res += str(digit_sum % 10)
            add_on = digit_sum // 10

        if add_on != 0:
            res += '1'

        ## return the reversed string
        return res[::-1]