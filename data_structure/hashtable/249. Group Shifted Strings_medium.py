'''

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
'''


class Solution:
    def __init__(self, ):
        self.letter_dict = {}
        for i, l in enumerate('abcdefghijklmnopqrstuvwxyz'):
            self.letter_dict[l] = i

    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        res_dict = collections.defaultdict(list)

        for str in strings:
            key = [0]
            for i, s in enumerate(str[1:]):
                pos = self.letter_dict[str[i + 1]] - self.letter_dict[str[i]]
                key.append(
                    pos if pos > 0 else 26 + pos
                )
            res_dict[tuple(key)].append(str)

        return list(res_dict.values())