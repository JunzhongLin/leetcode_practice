'''
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

'''


class Solution:
    def containsNearbyAlmostDuplicate_TLE(self, nums: List[int], k: int, t: int) -> bool:
        slow = 0
        fast = 0
        m = len(nums)

        while fast < m - 1:

            fast += 1
            if fast - slow > k:
                slow += 1

            for i in range(slow, fast, 1):
                if abs(nums[i] - nums[fast]) <= t:
                    return True

        return False