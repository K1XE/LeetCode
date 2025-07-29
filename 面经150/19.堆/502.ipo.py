#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
from mytools import *
# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w > max(capital):
            return w + sum(nlargest(k, profits))
        n = len(profits)
        tmp = [[capital[i], profits[i]] for i in range(n)]
        tmp.sort(key = lambda x : x[0])
        h = []
        cur = 0
        for _ in range(k):
            while cur < n and tmp[cur][0] <= w:
                heappush(h, -tmp[cur][1])
                cur += 1
            if h: w -= heappop(h)
            else: break
        return w
# @lc code=end

