'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''


class Solution:
    # time : O(n)
    # space: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i], plus = (digits[i] + 1 + plus) % 10, (digits[i] + 1 + plus) // 10
            else:
                digits[i], plus = (digits[i] + plus) % 10, (digits[i] + plus) // 10

        if plus == 1:
            digits = [1] + digits

        return digits