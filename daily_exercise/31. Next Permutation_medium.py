class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        i = len(nums) - 1

        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j < len(nums) and nums[j] > nums[i - 1]:
                    j += 1
                nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                return
            else:
                i -= 1

        nums.reverse()