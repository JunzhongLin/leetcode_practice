'''


'''


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        m, total_days = len(jobDifficulty), d

        if d > len(jobDifficulty):
            return -1

        @lru_cache(maxsize=None)
        def dp(jobDifficulty, d):
            if d == len(jobDifficulty):
                return sum(jobDifficulty)
            elif d == 1:
                return max(jobDifficulty)

            n = len(jobDifficulty)
            score = float(inf)

            for i in range(d - 1, n, 1):
                print(i, d - 1)
                score = min(score, dp(tuple(jobDifficulty[:i]), d - 1) + max(jobDifficulty[i:]))

            return score

        return dp(tuple(jobDifficulty), d)