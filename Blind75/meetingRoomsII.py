from collections import defaultdict
from heapq import heappush, heappop
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        meetings_at = defaultdict(int)

        for interval in intervals:
            meetings_at[interval.start] += 1
            meetings_at[interval.end] -= 1

        timelines = list(meetings_at.items())
        timelines.sort()

        ans = timelines[0][1]
        curr_sum = timelines[0][1]
        for i in range(1, len(timelines)):
            curr_sum += timelines[i][1]
            ans = max(ans, curr_sum)

        return ans

    def minMeetingRooms2(self, intervals):
        intervals.sort(key=lambda x: x.start)
        active_heap = []

        ans = 0
        for interval in intervals:
            while active_heap and active_heap[0][0] < interval.start:
                heappop(active_heap)

            heappush(active_heap, (interval.end, interval.start))
            ans = max(ans, len(active_heap))

        return ans


"""
[[1,4], [2,5], [7,9]]

1 -> 1
2 -> 1
4 -> -1
5 -> -1
7 -> 1
9 -> -1



"""
