from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.R = []  # min heap
        self.L = []  # max heap

    def addNum(self, num: int) -> None:
        if self.R:
            min_r_value = self.R[0]
            if min_r_value <= num:
                heappush(self.R, num)
            else:
                heappush(self.L, -num)
        else:
            heappush(self.R, num)

        # balancing
        if len(self.L) - len(self.R) > 1:
            heappush(self.R, -heappop(self.L))

        elif len(self.R) - len(self.L) > 1:
            heappush(self.L, -heappop(self.R))

    def findMedian(self) -> float:
        if len(self.R) > len(self.L):
            return self.R[0]
        elif len(self.L) > len(self.R):
            return -self.L[0]
        else:
            return (self.R[0] + -self.L[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()