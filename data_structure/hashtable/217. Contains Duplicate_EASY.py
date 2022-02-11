'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False