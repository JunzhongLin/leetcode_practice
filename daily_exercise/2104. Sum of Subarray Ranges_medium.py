from typing import List
# from collections import defaultdict

class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:

        range_list, increment, res = [(nums[0], nums[0])], 0, 0

        for i in range(1, len(nums), 1):
            # print(i)
            for j in range(len(range_list) - 1, -1, -1):
                # print([nums[i], range_list[j]])
                if nums[i] > range_list[j][1]:
                    increment = increment + nums[i] - range_list[j][1]
                    range_list[j] = (range_list[j][0], nums[i])

                elif nums[i] < range_list[j][0]:
                    increment = increment + range_list[j][0] - nums[i]
                    range_list[j] = (nums[i], range_list[j][1])

                else:
                    break
            res += increment
            range_list.append((nums[i], nums[i]))

        return res