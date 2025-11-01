#
# @lc app=leetcode.cn id=2517 lang=python3
#
# [2517] 礼盒的最大甜蜜度
#
from mytools import *
# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        def ck(x):
            lxt = price[0]
            cnt = 1
            for i in range(1, n):
                if price[i] - lxt >= x:
                    cnt += 1
                    lxt = price[i]
                    if cnt >= k: return True
            return False
        l, r = 0, price[-1] - price[0]
        while l <= r:
            mid = l + r >> 1
            if ck(mid): l = mid + 1
            else: r = mid - 1
        return r
# @lc code=end

