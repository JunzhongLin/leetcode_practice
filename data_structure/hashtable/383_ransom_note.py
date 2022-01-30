'''

Given two stings ransomNote and magazine, return true if ransomNote can be constructed
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r_counts = Counter(ransomNote)
        m_counts = Counter(magazine)
        x = r_counts-m_counts
        if len(x) == 0:
            return True
        else:
            return False

        # intersect_counts = r_counts & m_counts
        # for char in r_counts:
        #     if char not in intersect_counts:
        #         return False
        #     elif r_counts[char] > intersect_counts[char]:
        #         return False
        return True

