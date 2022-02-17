'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        i = -1
        for i in range(min([len(word) for word in strs])):
            for word in strs[1:]:
                if word[i] != strs[0][i]:
                    return word[:i]

        if i == -1:
            return ''

        return strs[0][:i + 1]