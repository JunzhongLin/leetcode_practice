from typing import List


class Solution:
    def trap_tle(self, height: List[int]) -> int:

        def helper(sub_height):

            if len(sub_height) <= 2:
                return 0

            if sub_height[-1] <= sub_height[-2]:
                return helper(sub_height[:-1])

            else:
                compared_height = sub_height[-2]
                res = helper(sub_height[:-1])
                for pos, height in enumerate(sub_height[-3::-1]):

                    if sub_height[-1] > height > compared_height:
                        res += (pos + 1) * (height - compared_height)
                        compared_height = height

                    elif height >= sub_height[-1]:
                        res += (pos + 1) * (sub_height[-1] - compared_height)
                        break

            return res

        return helper(height)

    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        stack = [(height[0], 0)]
        ans = 0

        for idx_, height in enumerate(height[1:]):
            while stack and height > stack[-1][0]:
                st_top_height, st_top_idx_ = stack.pop()
                if stack:
                    ans += (idx_ - stack[-1][1]) * (min(height, stack[-1][0]) - st_top_height)

            stack.append((height, idx_ + 1))

        return ans

height_1 = [4,2,0,3,2,5]
height_2 = [4,2,0,0,3,2,5]
ans_1 = Solution().trap(height_1)
ans_2 = Solution().trap(height_2)


