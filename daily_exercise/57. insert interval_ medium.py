from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # newInterval=[6, 10], left: [x, <6] or None,  right [>10, y] or None
        # left_boundary : left most intervals overlapped with newInterval
        # rigth_boundary: right most intervals overlapped with newInterval

        if len(intervals) == 0:
            return [newInterval]

        left_boundary, right_boundary = 0, len(intervals) - 1

        # searching for left boundray:
        left, right = 0, len(intervals) - 1

        if intervals[left][1] >= newInterval[0]:
            if intervals[left][0] <= newInterval[1]:
                left_boundary = 0
            else:
                return [newInterval] + intervals

        else:
            while right - left > 1:

                mid = (left + right) // 2
                if intervals[mid][1] < newInterval[0]:
                    left = mid
                elif intervals[mid][1] > newInterval[0]:
                    right = mid
                else:
                    left_boundary = mid
                    break

            if right - left == 1:
                left_boundary = right

        # searching for right boundary

        left, right = 0, len(intervals) - 1

        if intervals[right][0] <= newInterval[1]:
            if intervals[right][1] >= newInterval[0]:
                right_boundary = len(intervals) - 1

            else:
                return intervals + [newInterval]
        else:
            while right - left > 1:

                mid = (left + right) // 2

                if intervals[mid][0] < newInterval[1]:
                    left = mid
                elif intervals[mid][0] > newInterval[1]:
                    right = mid
                else:
                    right_boundary = mid
                    break

            if right - left == 1:
                right_boundary = left

        if right_boundary < left_boundary:
            return intervals[:right_boundary + 1] + [newInterval] + intervals[left_boundary:]

        else:
            if newInterval[1] >= intervals[right_boundary][1]:
                right_limit = newInterval[1]
            else:
                right_limit = intervals[right_boundary][1]

            if newInterval[0] <= intervals[left_boundary][0]:
                left_limit = newInterval[0]
            else:
                left_limit = intervals[left_boundary][0]

            return intervals[:left_boundary] + [[left_limit, right_limit]] + intervals[right_boundary + 1:]


class Solution_n:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output