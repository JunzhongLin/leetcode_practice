class Solution:

    def __init__(self, w: List[int]):
        self.length = sum(w)
        self.n = len(w)
        self.w_pool = [0]
        for i in range(self.n):
            self.w_pool.append(self.w_pool[-1] + w[i])

    def pickIndex(self) -> int:
        picked_val = random.uniform(0, self.length)
        i = 0
        left, right = 0, self.n
        while left < right - 1:
            mid = (right + left) // 2
            if picked_val == self.w_pool[mid]:
                return mid - 1
            elif picked_val > self.w_pool[mid]:
                left = mid
            elif picked_val < self.w_pool[mid]:
                right = mid

        return left