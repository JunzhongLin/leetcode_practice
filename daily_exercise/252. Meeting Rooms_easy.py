'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] >= end:
                start, end = interval
                continue
            else:
                return False

        return True

