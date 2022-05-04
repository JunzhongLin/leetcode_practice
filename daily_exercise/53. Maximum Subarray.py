'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')

        for i in range(len(nums)):
            if i and nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_val = max(max_val, nums[i])

        return max_val