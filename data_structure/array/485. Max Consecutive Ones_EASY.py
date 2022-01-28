'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

'''


class Solution:

    def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        res_temp = 0
        for num in nums:
            if num == 1:
                res_temp +=1
                if res_temp > res:
                    res = res_temp
            else:
                res_temp = 0
        return res