class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate_dict = {
            '6': '9',
            '9': '6',
            '1': '1',
            '8': '8',
            '0': '0'
        }
        res = ''
        for digit in num:
            if digit not in rotate_dict:
                return False

            res += rotate_dict[digit]

        if res[::-1] == num:
            return True

        return False