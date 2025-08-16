#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
from mytools import *
# @lc code=start
class MedianFinder:
    
    def __init__(self):
        self.l ,self.r = [], []
        heapq.heapify(self.l)
        heapq.heapify(self.r)

    def addNum(self, num: int) -> None:
        if len(self.l) == len(self.r):
            heapq.heappush(self.r, num)
            heapq.heappush(self.l, -heapq.heappop(self.r))
        else:
            heapq.heappush(self.l, -num)
            heapq.heappush(self.r, -heapq.heappop(self.l))

    def findMedian(self) -> float:
        n = len(self.l) + len(self.r)
        if n % 2: return -self.l[0]
        else: return (-self.l[0] + self.r[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

