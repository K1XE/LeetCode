#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
from mytools import *
# @lc code=start
class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if len(self.r) > len(self.l):
            heappush(self.l, -heappop(self.r))

    def findMedian(self) -> float:
        n = len(self.l) + len(self.r)
        if n & 1: return -self.l[0]
        else: return (self.r[0] - self.l[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

