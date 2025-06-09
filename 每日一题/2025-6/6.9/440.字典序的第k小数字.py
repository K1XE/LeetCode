#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#
from mytools import *
# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(l, r):
            cur = l
            nxt_l = l + 1
            cnt = 0
            while cur <= r:
                cnt += min(nxt_l, r + 1) - cur
                cur *= 10
                nxt_l *= 10
            return cnt
        cur = 1
        k -= 1
        while k > 0:
            cnt = get_count(cur, n)
            if k >= cnt:
                cur += 1
                k -= cnt
            else:
                cur *= 10
                k -= 1
        return cur
# @lc code=end

