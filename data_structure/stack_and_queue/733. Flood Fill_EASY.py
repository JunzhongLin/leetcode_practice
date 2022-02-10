'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

'''


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image == [[]]:
            return image

        stack = [(sr, sc)]
        m = len(image)
        n = len(image[0])
        visited = set()
        raw_color = image[sr][sc]

        while stack:

            i, j = stack.pop()

            for ii, jj in (i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and image[ii][jj] == raw_color:
                    image[ii][jj] = newColor
                    visited.add((ii, jj))
                    stack.append((ii, jj))
        return image