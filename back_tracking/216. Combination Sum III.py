'''
Find all valid combinations of k numbers that sum up to n such that the following
conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the
same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

'''

class Solution:

    def sum_combine(self, n, k):
        answers = []
        ans = []

        def backtracking(n, k, sum_, startindex):

            if sum_ > n: return

            if len(ans) == k and sum_ == n:
                answers.append(ans[:])
                return


            for i in range(startindex, 9-(k-len(ans))+2):
                ans.append(i)
                sum_ += i
                backtracking(n, k, sum_, i+1)
                sum_ -= i
                ans.pop()

        backtracking(n, k, 0, 1)

        return answers


if __name__ == '__main__':
    n = 10
    k = 2
    res = Solution().sum_combine(n, k)
    print(res)