from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 0, 1, 2, 3, 2, 1, 0, 1, 2 ,3 ,2 ,1 , 0, 1,2,3,2,1,0
        # 0:2, 1:1, 2:0, 3:1, 2
        # 0, 1, 2 , 1 ,0, 1, 2, 1, 0

        if numRows == 1:
            return s

        res_lists_dict, res_lists_que, res = {}, [i for i in range(numRows - 1)], ''
        for i in range(numRows):
            res_lists_dict[i] = []

        for j in range(len(s)):
            k = res_lists_que.pop(0)
            res_lists_dict[k].append(s[j])
            res_lists_que.append(numRows - 1 - k)

        for i in range(numRows):
            res += ''.join(res_lists_dict[i])

        return res