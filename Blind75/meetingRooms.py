class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            # if overlapping
            if curr.start < prev.end:
                return False

        return True
