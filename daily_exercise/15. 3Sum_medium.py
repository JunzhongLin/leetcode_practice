'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = set()

        nums = sorted(nums)
        # print(nums)

        for i, num in enumerate(nums[:-2]):
            left, right = i + 1, len(nums) - 1
            if num > 0:
                return res
            while left < right:
                # print(num, nums[left], nums[right])
                if nums[left] > -num:
                    return res
                elif nums[left] + nums[right] < -num:
                    left += 1
                elif nums[left] + nums[right] > -num:
                    right -= 1
                elif nums[left] + nums[right] == -num:
                    res.add((num, nums[left], nums[right]))
                    if nums[left] == nums[left + 1]:
                        left += 1
                    else:
                        right -= 1
        return list(res)
