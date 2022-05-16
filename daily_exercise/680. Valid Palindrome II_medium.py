class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = 0

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                deleted += 1
                if deleted >= 2:
                    return False

                checkpoint = (left, right)

                left += 1
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                        if left >= right:
                            return True
                    else:
                        break

                left, right = checkpoint
                right -= 1
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                        if left >= right:
                            return True
                    else:
                        break

        return True