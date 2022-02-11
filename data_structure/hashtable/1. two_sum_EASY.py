# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


class Solution:
    def two_sum(self, num, target) -> object:
        map = {}
        for ind, val in enumerate(num):
            map[val]=ind
            diff = target - val
            if diff in map.keys():
                print([map[diff], ind])
                return [map[diff], ind]

if __name__=='__main__':
    sol = Solution()
    sol.two_sum([5,7,2,4,8], 6)

