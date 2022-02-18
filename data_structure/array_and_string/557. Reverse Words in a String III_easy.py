'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

'''


class Solution:
    def reverseWords(self, s: str) -> str:

        left, right = 0, len(s) - 1
        d, word = deque(), []

        while left <= right:
            if s[left] == ' ' and word:
                d.append(''.join(reversed(word)))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.append(''.join(reversed(word)))

        return ' '.join(d)