'''

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''


class Solution:
    def reverseWords(self, s: str) -> str:

        left, right = 0, len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)