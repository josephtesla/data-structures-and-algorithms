class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pure = [intervals[0]]
        ans = 0
        for [start, end] in intervals[1:]:
            lastMergedEnd = pure[-1][1]
            if start < lastMergedEnd:
                pure[-1][1] = min(end, lastMergedEnd)
                ans += 1
            else:
                pure.append([start, end])

        return ans


a = [55, 63, 6, 72, 53, 66]

print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))