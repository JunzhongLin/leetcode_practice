'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity

'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = -1, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            elif nums[mid] >= target:
                right = mid

        if nums[right] == target:
            ans_left = right
        else:
            return [-1, -1]

        left, right = left + 1, len(nums)
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                left = mid

        ans_right = right - 1
        return [ans_left, ans_right]