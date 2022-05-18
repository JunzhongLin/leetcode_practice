class SparseVector:
    def __init__(self, nums: List[int]):
        pos, val = [], []
        for i in range(len(nums)):
            if nums[i] != 0:
                pos.append(i)
                val.append(nums[i])

        self.svector = [len(nums), pos, val]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if self.svector[1] == [] or vec.svector[1] == []:
            return ans
        i, j = 0, 0
        while i < len(self.svector[1]) and j < len(vec.svector[1]):
            if self.svector[1][i] == vec.svector[1][j]:
                ans += self.svector[2][i] * vec.svector[2][j]
                i += 1
                j += 1
            elif self.svector[1][i] < vec.svector[1][j]:
                i += 1
            else:
                j += 1
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)