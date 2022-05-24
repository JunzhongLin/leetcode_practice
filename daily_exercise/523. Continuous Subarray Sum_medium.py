class Solution:
    def checkSubarraySum_tle(self, nums, k: int) -> bool:
        # time: O(n**2)
        # space: O(n)
        if len(nums) == 1:
            return False

        remainder_set = {nums[0] % k}

        for num in nums[1:]:
            if (k - num % k) % k in remainder_set:
                return True

            else:
                for remainder in list(remainder_set):
                    remainder_set.remove(remainder)
                    remainder_set.add((remainder + num % k) % k)
                remainder_set.add(num % k)

        return False

    def checkSubarraySum(self, nums, k):
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):

            summ = (summ + n) % k

            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

'''
2, 11, [10]
4, 9, [12, 2]
6, 7, [3, 6, 4]
7, 6, [9, 12, 10, 6]
'''


a= [23,2,6,4,7]

b = Solution().checkSubarraySum(a, 13)