'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.



Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        que = []
        res = 0
        flipped = False
        i_zero = 0

        for num in nums:
            if num == 1:
                que.append(num)
                res = max(res, len(que))
            elif num == 0 and not flipped:
                que.append(num)
                flipped = True
                i_zero = len(que) - 1
                res = max(res, len(que))
            elif num == 0 and flipped:
                res = max(res, len(que))
                del que[:i_zero + 1]
                que.append(num)
                i_zero = len(que) - 1
        return res
