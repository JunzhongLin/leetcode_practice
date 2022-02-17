'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

'''


class Solution:
    # time : O(n) -- n is the length of nums list
    # space: O(1)
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        if not nums:
            return -1

        left_sum = 0
        right_sum = sum(nums[1:])

        if left_sum == right_sum:
            return 0

        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        return -1