'''

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1_counts = collections.Counter(nums1)
        for num in nums2:
            if num in nums1_counts and nums1_counts[num]>=1:
                res.append(num)
                nums1_counts[num] -= 1
        return res