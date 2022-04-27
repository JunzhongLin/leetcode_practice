class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        for i in range(len(nums)):

            que = [([nums[i]], i)]

            while que:
                init_num, j = que.pop(0)
                res.append(init_num)
                if j == n - 1:
                    continue

                for ii in range(j + 1, n):
                    temp = []
                    temp = init_num + [nums[ii]]
                    que.append((temp, ii))

        return res