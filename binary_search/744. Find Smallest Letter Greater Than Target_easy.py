'''

Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1
        if letters[right] <= target:
            return letters[0]
        if letters[left] > target:
            return letters[left]

        while left < right - 1:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            elif letters[mid] <= target:
                left = mid

        return letters[right]