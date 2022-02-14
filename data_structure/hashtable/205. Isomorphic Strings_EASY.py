'''

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''


class Solution(object):
    def isIsomorphic_temp(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map, l_map = {}, {}

        if len(s) != len(t):
            return False

        for s_l, t_l in zip(s, t):
            if s_l not in s_map and t_l not in l_map:
                s_map[s_l] = t_l
                l_map[t_l] = s_l
            elif (s_l in s_map and s_map[s_l] != t_l) or (t_l in l_map and l_map[t_l] != s_l):
                return False

        return True

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        if len(s) != len(t):
            return False
        for s_l, t_l in zip(s, t):
            if s_l not in s_map and t_l not in s_map.values():
                s_map[s_l] = t_l
            elif (s_l in s_map and s_map[s_l] != t_l) or (s_l not in s_map and t_l in s_map.values()):
                return False
        return True