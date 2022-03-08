'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums) - 1
        if nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1]:
            return right

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1