from collections import Counter, deque
from heapq import heappop, heappush


class Solution:
    def leastInterval(self, tasks: [str], n: int):
        task_counts = Counter(tasks)
        task_heap = []
        for k, v in task_counts.items():
            heappush(task_heap, -v)

        time = 0
        positions = dict()

        while task_heap or len(positions):
            time += 1
            if task_heap:
                cnt = -heappop(task_heap) - 1
                if cnt != 0:
                    positions[time + n] = cnt

            if time in positions:
                heappush(task_heap, -positions[time])
                del positions[time]

        return time



print(Solution().leastInterval(["A","A","A","B","B","B"], 2))

