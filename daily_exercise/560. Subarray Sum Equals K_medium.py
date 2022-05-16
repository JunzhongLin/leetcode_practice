class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        sum_tmp, ans = 0, 0
        hashmap[sum_tmp] += 1
        for num in nums:
            sum_tmp += num
            if (sum_tmp - k) in hashmap:
                ans += hashmap[sum_tmp-k]
            hashmap[sum_tmp] += 1
        return ans