'''

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sub_res = [], []

        def backtrack_combinations(s, n, k, res, sub_res):
            for num in range(s, n + 1):
                if k > 0:
                    sub_res.append(num)
                    k -= 1
                    s += 1
                    if k == 0:
                        res.append(sub_res[:])
                    backtrack_combinations(s, n, k, res, sub_res)
                    sub_res.pop()
                    k += 1
            return res

        return backtrack_combinations(1, n, k, res, sub_res)