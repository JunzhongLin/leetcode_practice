'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
 The returned string should  only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

'''

class Solution:
    def reverseWords(self, s):

        def trim_spaces(s):
            left, right = 0, len(s)-1

            while left<right and s[left] == ' ':
                left += 1
            while left<right and s[right] == ' ':
                right -= 1

            temp = []
            while left<=right:
                if s[left] != ' ':
                    temp.append(s[left])
                elif s[left] == ' ' and temp[-1] != ' ':
                    temp.append(' ')
                left += 1

            return temp

        def words_split(s):
            res = []
            temp = []
            index_ = 0
            while index_ <= len(s)-1:
                if s[index_] != ' ':
                    temp.append(s[index_])
                    index_ += 1

                elif s[index_] == ' ':
                    res.append(''.join(temp))
                    temp = []
                    while s[index_] == ' ' and index_ <= len(s)-1:
                        index_+=1
                    res.append(' ')
                if index_ == len(s):
                    res.append(''.join(temp))

            return res

        def reverse_single_word(list_words):
            left, right = 0, len(list_words)-1
            while left <= right:
                list_words[left], list_words[right] = list_words[right], list_words[left]
                left += 1
                right -= 1
            return list_words

        temp = trim_spaces(s)
        list_ = words_split(temp)
        reverse_list_ = reverse_single_word(list_)

        return ''.join(reverse_list_)


if __name__ == '__main__':
    s = '   this   is a test  '
    res= Solution().reverseWords(s)