'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

'''
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        count = 0
        target_depth = len(nums) - 1
        stack = [(0, -1, 0)]
        cache = defaultdict(int)

        while stack:
            # print(stack)
            # count += 1
            # if count == 10:
            #     break
            curr_sum, depth, visited = stack.pop()

            if visited:
                if depth == target_depth:
                    if curr_sum == target:
                        cache[(curr_sum, depth, visited)] = 1
                else:
                    l = cache[(curr_sum + nums[depth + 1], depth + 1, 1)]
                    r = cache[(curr_sum - nums[depth + 1], depth + 1, 1)]
                    cache[(curr_sum, depth, visited)] = l + r
                    continue
            else:
                if (curr_sum, depth, 1) in cache:
                    continue

                stack.append((curr_sum, depth, 1))

                if depth < target_depth:
                    stack.append((curr_sum + nums[depth + 1], depth + 1, 0))
                    stack.append((curr_sum - nums[depth + 1], depth + 1, 0))

        return cache[(0, -1, 1)]


input_val, target = [1,1,1,1,1], 3

res = Solution().findTargetSumWays(input_val, target)