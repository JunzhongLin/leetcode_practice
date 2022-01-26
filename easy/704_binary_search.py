'''
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''

class Solution:

    def binary_search(self, nums, target):
        left, right = (0, len(nums))
        ans = -1
        while left < right:
            middle = (right-left)//2 + left
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            elif nums[middle] == target:
                ans = middle
                break

        return ans


class Solution_2: #  []
    def search(self, nums) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

'''
[1,2,3]
m=1 --> 1, 2
m=0
'''


if __name__ == '__main__':
    nums = [1,2,3,4,6,7,8,9,10]
    target = 11
    ans = Solution().binary_search(nums, target)