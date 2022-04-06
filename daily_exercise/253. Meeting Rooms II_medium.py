'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

'''


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals )==0:
            return 0
        elif len(intervals )==1:
            return 1

        intervals = sorted(intervals, key=lambda x :x[0])
        res = 1
        start, end = intervals[0]
        ends = [end]

        for interval in intervals[1:]:
            ends = sorted(ends)
            while ends:
                if interval[0] < ends[0]:
                    ends.append(interval[1])
                    res = max(res, len(ends))
                    break
                else: ends.pop(0)

            if not ends:
                ends = [interval[1]]
        return res
