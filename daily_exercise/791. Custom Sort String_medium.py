class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # time : O(s.length + order.length)
        # space O(order.length)

        from collections import defaultdict
        s_dict = defaultdict(int)
        res = ''

        for cha in s:
            s_dict[cha] += 1

        for cha in order:
            if cha in s_dict and s_dict[cha] != 0:
                res += cha * s_dict[cha]
                s_dict[cha] = 0
            else:
                continue

        for cha in s_dict.keys():
            res += cha * s_dict[cha]

        return res