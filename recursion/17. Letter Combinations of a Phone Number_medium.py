'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }
        ans, n = [], len(digits)

        def backtracking(digits, sub_ans):
            if len(digits) == 0:
                return None
            for l in letter_map[digits[0]]:
                sub_ans.append(l)
                # print(sub_ans)
                if len(sub_ans) == n:
                    ans.append(''.join(sub_ans[:]))
                backtracking(digits[1:], sub_ans)
                sub_ans.pop()

        backtracking(digits, [])

        return ans