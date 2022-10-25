from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        non_zero_set = set()

        for num in nums:
            if num not in non_zero_set and num != 0:
                non_zero_set.add(num)

        return len(list(non_zero_set))