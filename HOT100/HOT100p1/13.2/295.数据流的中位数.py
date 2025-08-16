#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
from mytools import *
# @lc code=start
class MedianFinder:

    def __init__(self):
        self.hmin = []
        self.hmax = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.hmax, -num)
        heapq.heappush(self.hmin, -heapq.heappop(self.hmax))
        if len(self.hmin) > len(self.hmax):
            heapq.heappush(self.hmax, -heapq.heappop(self.hmin))
    def findMedian(self) -> float:
        if len(self.hmax) + len(self.hmin) & 1: return -self.hmax[0]
        else: return (self.hmin[0] - self.hmax[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

