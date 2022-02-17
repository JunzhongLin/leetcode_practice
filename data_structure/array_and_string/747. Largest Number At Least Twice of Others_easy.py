'''

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
'''


class Solution:
    ## time : O(log(n) +n) = O(n)
    #  space O(n)
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        sorted_nums = nums[:]
        sorted_nums.sort()
        if sorted_nums[-1] >= sorted_nums[-2] * 2:
            for i, num in enumerate(nums):
                if num == sorted_nums[-1]:
                    return i

        return -1