'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

class Solution:
    def intersect_array(self, num1, num2):
        from collections import Counter
        num1_dict = Counter(num1)
        num2_dict = Counter(num2)
        intersect_dict = num2_dict & num1_dict
        res = []
        for k in intersect_dict:
            res.append(k)
        return res

    def intersect_array_set(self, num1, num2):
        return list(set(num1) & set(num2))