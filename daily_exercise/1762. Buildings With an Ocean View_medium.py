class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        max_height = 0

        for i in range(len(heights) - 1, 0, -1):
            max_height = max(max_height, heights[i])
            if heights[i - 1] > max_height:
                res.append(i - 1)

        res.reverse()
        return res