class Solution:
    def canJump_td(self, nums: List[int]) -> bool:

        n = len(nums)

        def dp(i):
            if i == 0:
                return True

            need_length = 0
            while i > 0:
                i -= 1
                need_length += 1

                if nums[i] >= need_length:
                    return dp(i)

            return False

        return dp(n - 1)

    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True

        max_jump_sofar = nums[0]

        for i in range(1, len(nums)):

            if max_jump_sofar >= 1:
                dp[i] = True
                max_jump_sofar = max(max_jump_sofar - 1, nums[i])

            else:
                break

        return dp[n - 1]