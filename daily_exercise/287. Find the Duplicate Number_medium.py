class Solution:
    def findDuplicate_hash(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
            if num_dict[num] > 1:
                return num

    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate

