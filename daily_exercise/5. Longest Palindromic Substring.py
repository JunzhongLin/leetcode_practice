'''

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_ans = 1
        ans = s[0]
        visited = defaultdict(list)
        for i, letter in enumerate(s):
            visited[letter].append(i)

        for j in range(len(s) - 1, -1, -1):
            if s[j] in visited:
                for start in visited[s[j]]:
                    if j - start + 1 > len_ans:
                        tmp = list(s[start:j + 1])
                        tmp.reverse()
                        if list(s[start:j + 1]) == tmp:
                            ans = s[start:j + 1]
                            len_ans = j - start + 1
                            break
        return ans