'''

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stack = [s]
        word_set = set(wordDict)
        max_len_word = len(sorted(wordDict, key=lambda x: len(x))[-1])
        visited = set()

        while stack:
            candidate = stack.pop()

            for i in range(len(candidate)):
                if candidate[:i + 1] in word_set and i + 1 <= max_len_word:
                    if len(candidate[i + 1:]) == 0:
                        return True
                    elif candidate[i + 1:] in visited:
                        continue
                    stack.append(candidate[i + 1:])
                    visited.add(candidate[i + 1:])
                elif i + 1 > max_len_word:
                    break
        return False