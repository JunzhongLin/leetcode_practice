'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution:
    def search_iter(self, nums: List[int], target: int) -> int:
        que = [nums]
        center = 0
        while que:
            lst = que.pop(0)
            if len(lst) < 1:
                return -1
            if lst[len(lst) // 2] == target:
                return center + len(lst) // 2
            elif lst[len(lst) // 2] > target:
                que.append(lst[:len(lst) // 2])
            elif lst[len(lst) // 2] < target:
                center += len(lst) // 2 + 1
                que.append(lst[(len(lst) // 2 + 1):])

    def search(self, nums: List[int], target: int) -> int:

        def helper(lst, center):
            if len(lst) < 1:
                return -1
            if lst[len(lst) // 2] == target:
                return center + len(lst) // 2
            elif lst[len(lst) // 2] > target:
                return helper(lst[:len(lst) // 2], center)
            elif lst[len(lst) // 2] < target:
                center += len(lst) // 2 + 1
                return helper(lst[(len(lst) // 2 + 1):], center)

        return helper(nums, 0)