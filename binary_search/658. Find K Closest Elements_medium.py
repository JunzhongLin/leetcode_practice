'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        # tmp = [abs(i-x) for i in arr]
        index = None

        left, right = 0, len(arr) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if arr[mid] - x < 0:
                left = mid
            elif arr[mid] == x:
                index = mid
                break
            else:
                right = mid

        if not index:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                index = left
            else:
                index = right

        left, right = index, index

        while k - 1 > 0:
            if left == 0:
                return arr[left:right + k]
            if right == len(arr) - 1:
                return arr[left - k + 1:]

            if abs(arr[right + 1] - x) < abs(arr[left - 1] - x):
                right += 1
                k -= 1
            elif abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                left -= 1
                k -= 1

        return arr[left:right + 1]