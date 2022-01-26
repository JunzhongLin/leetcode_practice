'''
Given two integers n and k, return all possible combinations of k numbers out
of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

class Solution:
    def combine(self, n: int, k: int):
        results = []
        path = []

        def backtracking(n, k, startindex):
            if len(path) == k:
                results.append(path[:])
                return
            for i in range(startindex, n-(k-len(path))+2):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
        backtracking(n, k, 1)

        return results

if __name__== '__main__':
    n, k = 4, 2
    res = Solution().combine(n, k)