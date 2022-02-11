'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        found_duplicates = False
        nums.sort()

        for i in range(len(nums) - 1):
            if found_duplicates and nums[i + 1] != nums[i]:
                found_duplicates = False
                continue

            if not found_duplicates and nums[i + 1] != nums[i]:
                return nums[i]

            if nums[i + 1] == nums[i]:
                found_duplicates = True

        return nums[-1]