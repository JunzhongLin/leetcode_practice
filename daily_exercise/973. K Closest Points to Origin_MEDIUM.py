class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # time: O(N*log(N))
        # space: O(N)
        #
        points.sort(key=lambda x : sqrt(x[0]**2+x[1]**2))
        return points[:k]