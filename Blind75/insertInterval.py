class Solution:
    def insert_into_output(self, output, interval):
        if output:
            # if it overlaps
            if output[-1][1] >= interval[0]:
                output[-1][1] = max(output[-1][1], interval[1])  # merge
            else:
                output.append(interval)
        else:
            output.append(interval)

    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        output = []
        added = False

        # if len(intervals) == 0 = newInterval[0] < intervals[0][0]:
        for [start, end] in intervals:

            # check and process new interval in its sorted position
            if start > newInterval[0] and not added:
                self.insert_into_output(output, newInterval)
                added = True

            # process current interval
            self.insert_into_output(output, [start, end])

        if not added:
            self.insert_into_output(output, newInterval)

        return output
