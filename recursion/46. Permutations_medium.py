'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_set = set(nums)

        def backtracking(nums, sub_ans):
            for num in nums:
                if num in nums_set:
                    sub_ans.append(num)
                    nums_set.remove(num)
                    # print(sub_ans, nums_set)
                    if len(sub_ans) == len(nums):
                        ans.append(sub_ans[:])
                    backtracking(nums, sub_ans)
                    num = sub_ans.pop()
                    nums_set.add(num)
                    # print(nums_set)

        backtracking(nums, [])

        return ans