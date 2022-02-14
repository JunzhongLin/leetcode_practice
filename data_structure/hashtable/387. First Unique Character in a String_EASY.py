'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_str = collections.defaultdict(int)

        for index, cha in enumerate(s):
            map_str[cha] += 1

        for i in range(len(s)):
            if map_str[s[i]] == 1:
                return i

        return -1