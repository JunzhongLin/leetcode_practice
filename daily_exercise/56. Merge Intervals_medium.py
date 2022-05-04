'''

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals[:]

        intervals = sorted(intervals, key=lambda x: x[0])

        res = []

        for interval in intervals:

            if not res:
                res.append(interval)
            else:
                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(interval[1], res[-1][1])
                else:
                    res.append(interval)

        return res