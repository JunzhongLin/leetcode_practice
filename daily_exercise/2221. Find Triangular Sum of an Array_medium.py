from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        num_length = len(nums)

        for j in range(num_length - 1, 0, -1):
            for i in range(j):
                nums[i] = (nums[i] + nums[i + 1]) % 10

        return nums[i]