from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:

        char_dict, res, res_increment = defaultdict(list), 0, 0

        for i, char in enumerate(s):
            if char not in char_dict:
                res += res_increment + i + 1
                res_increment += i + 1
            else:
                res += res_increment - (char_dict[char][1]) + (i - char_dict[char][0] - 1) + 1
                res_increment += - (char_dict[char][1]) + (i - char_dict[char][0] - 1) + 1

            char_dict[char] = [i, i - char_dict[char][0] if char_dict[char] else i + 1]

        return res