from collections import defaultdict
from heapq import heappush, heappop, heapify

"""
Worst case --> O(N*LogN)
"""

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        freq = defaultdict(int)
        reverse_freq = defaultdict(list)

        for num in nums:
            freq[num] += 1

        for key, v in freq.items():
            reverse_freq[v].append(key)

        arr = list(reverse_freq.items())

        heapify(arr)

        n = len(arr)
        result = []

        for _ in range(n - k):
            heappop(arr)

        for _ in range(k):
            values = heappop(arr)
            result = values[1] + result

        return result[:k]





