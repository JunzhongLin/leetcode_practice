'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hash_map_12 = collections.defaultdict(int)
        n = len(nums1)
        res = 0

        for i in range(n):
            for j in range(n):
                hash_map_12[nums1[i] + nums2[j]] += 1

        for k in range(n):
            for l in range(n):

                if -nums3[k] - nums4[l] in hash_map_12:
                    res += hash_map_12[-nums3[k] - nums4[l]]

        return res


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = collections.defaultdict(int)
        lists = [A, B, C, D]

        def nSumCount() -> int:
            addToHash(0, 0)
            return countComplements(len(lists) // 2, 0)

        def addToHash(i: int, total: int) -> None:
            if i == len(lists) // 2:
                m[total] = m[total] + 1
            else:
                for a in lists[i]:
                    addToHash(i + 1, total + a)

        def countComplements(i: int, complement: int) -> int:
            if i == len(lists):
                return m[complement]
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(i + 1, complement - a)
            return cnt

        return nSumCount()