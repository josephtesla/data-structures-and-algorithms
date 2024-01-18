"""
Time Complexity --> O(N*LOG N)
Space Complexity ---> O(1)
"""


class Solution:
    def isOverlapping(self, a, b):
        return (a[0] <= b[1]) and (a[1] >= b[0])

    def mergeTwoOverlap(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

    def mergeEasy(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for [start, end] in intervals[1: ]:
            lastMergedEnd = output[-1][1]
            if start <= lastMergedEnd:
                output[-1][1] = max(lastMergedEnd, end)
            else:
                output.append([start, end])

        return output

    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        i = 0
        results = []

        # Go through intervals
        while i < len(intervals):
            # starting from the current
            # merge all following
            # intervals that overlap
            # since they are sorted by start time,
            # overlapping intervals will follow one another
            currentMerged = intervals[i]
            for k in range(i, len(intervals)):
                if self.isOverlapping(currentMerged, intervals[k]):
                    currentMerged = self.mergeTwoOverlap(currentMerged, intervals[k])
                    # if the current merging
                    # reaches the last interval.
                    # add the merged and return result
                    if k == len(intervals) - 1:
                        results.append(currentMerged)
                        return results
                else:
                    # if the next kth does not overlap.
                    # add the merged to result and move start position
                    # to kth
                    results.append(currentMerged)
                    i = k
                    break

        return results


print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
