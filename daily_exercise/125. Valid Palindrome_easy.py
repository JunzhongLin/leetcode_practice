class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        left, right = 0, len(s) - 1

        while left < right:

            # print('left: ',s[left], 'right: ', s[right])

            if s[left] not in letter_set:
                # print(left)
                left += 1
                continue
            if s[right] not in letter_set:
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True