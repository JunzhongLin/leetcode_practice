import math


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def cut_test(ribbons, length_, k):
            num_r = 0
            for r in ribbons:
                num_r += r // length_
            return num_r >= k

        length_ = max(ribbons)
        right = length_

        while length_ > 0:

            if cut_test(ribbons, length_, k):
                left = length_
                while left < right - 1:
                    mid = (left + right) // 2
                    if cut_test(ribbons, mid, k):
                        left = mid
                    else:
                        right = mid
                return left
            else:
                right = length_

            length_ = math.floor(length_ / 2)

        return 0