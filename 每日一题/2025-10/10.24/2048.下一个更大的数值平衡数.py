#
# @lc app=leetcode.cn id=2048 lang=python3
#
# [2048] 下一个更大的数值平衡数
#
from mytools import *
# @lc code=start
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(n):
            cnt = Counter(str(n))
            for k, v in cnt.items():
                if int(k) != v: return False
            return True
        n += 1
        while True:
            if check(n): return n
            n += 1
# @lc code=end

