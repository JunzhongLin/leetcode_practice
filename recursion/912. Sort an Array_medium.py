'''
Given an array of integers nums, sort the array in ascending order.

'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])

        return self.combineArray(left, right)

    def combineArray(self, list1, list2):
        res = []

        left, right = 0, 0

        while left < len(list1) and right < len(list2):
            if list1[left] < list2[right]:
                res.append(list1[left])
                left += 1
            else:
                res.append(list2[right])
                right += 1

        res.extend(list1[left:])
        res.extend(list2[right:])

        return res