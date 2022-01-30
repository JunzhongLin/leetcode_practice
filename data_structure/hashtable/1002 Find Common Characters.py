'''
Given a string array words, return an array of all characters that show up in all strings within the words
 (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

'''

class Solution:
    def find_common_char(self, words):
        from collections import Counter
        temp = Counter(words[0])
        for i in range(1, len(words)):
            counts = Counter(words[i])
            temp = temp & counts
        for k in temp:
            print(k+ ' : ', temp.get(k))
