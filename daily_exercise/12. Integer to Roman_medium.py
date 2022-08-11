class Solution:
    def intToRoman(self, num: int) -> str:
        trans_dict = {
            '1': 'I',
            '5': 'V',
            '10': 'X',
            '50': 'L',
            '100': 'C',
            '500': 'D',
            '1000': 'M'
        }

        len_num = len(str(num))
        res = ''
        for i, digit in enumerate(str(num)):
            i = len_num - i - 1
            if digit == '4':
                res += trans_dict['1' + i * '0'] + trans_dict['5' + i * '0']
            elif digit == '9':
                res += trans_dict['1' + i * '0'] + trans_dict['1' + (i + 1) * '0']
            elif int(digit) < 4:
                res += int(digit) * trans_dict['1' + i * '0']
            else:
                res += trans_dict['5' + i * '0'] + (int(digit) - 5) * trans_dict['1' + i * '0']

        return res
