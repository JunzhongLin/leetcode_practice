class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        slow, fast = 0, 1
        res = []
        start = [lower - 1]

        if not nums or nums[0] > lower:
            nums = start + nums
        if nums[-1] < upper:
            nums.append(upper + 1)

        if len(nums) == 1:
            return []

        while fast < len(nums):
            if nums[fast] - nums[slow] == 2:
                res.append('{}'.format(nums[slow] + 1))
            elif nums[fast] - nums[slow] > 2:
                res.append('{}->{}'.format(nums[slow] + 1, nums[fast] - 1))

            slow += 1
            fast += 1

        return res

