'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

'''


class Solution:
    # O(n)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0, 0
        c_sum = 0
        res = len(nums) + 1
        for _ in range(len(nums)):
            while c_sum < target and fast < len(nums):
                fast += 1
                c_sum += nums[fast - 1]
            if c_sum >= target:
                res = min(fast - slow, res)
                c_sum -= nums[slow]
                slow += 1
                continue
            break

        if res > len(nums):
            return 0

        return res