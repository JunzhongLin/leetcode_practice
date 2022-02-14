'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        hash_map = collections.Counter(nums)
        return [x for x, y in hash_map.most_common(k)]