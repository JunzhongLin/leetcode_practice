'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

'''

class Solution:
    def __init__(self,):
        self.results = []
        self.path = ''
        self.string_map_ = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def _backtracking(self, digits, startindex):

        if len(self.path) == len(digits):
            self.results.append(self.path[:])
            print(self.results)
            return

        for letter in self.string_map_[digits[startindex]]:
            self.path += letter
            self._backtracking(digits, startindex + 1)
            self.path = self.path[:-1]

            # self.path.append(letter)
            # self._backtracking(digits, startindex + 1)
            # self.path.pop()

    def letterCombinations(self, digits):

        self._backtracking(digits, 0)

        return self.results

if __name__=='__main__':
    digits = '23'
    res = Solution().letterCombinations(digits)