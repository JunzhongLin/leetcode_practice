'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

'''


class Solution:
    # time O(n)
    # space O(1)
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        slow, fast = 0, 1
        max_sum = 0
        while fast <= len(nums) - 1:
            max_sum += min(nums[slow], nums[fast])
            slow += 2
            fast += 2

        return max_sum