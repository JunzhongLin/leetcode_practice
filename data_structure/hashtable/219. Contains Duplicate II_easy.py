'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashset = set()

        for i in range(n):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            if len(hashset) > k:
                hashset.remove(nums[i - k])

        return False