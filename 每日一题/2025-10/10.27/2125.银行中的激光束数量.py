#
# @lc app=leetcode.cn id=2125 lang=python3
#
# [2125] 银行中的激光束数量
#
from mytools import *
# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = cnt = res = 0
        for i, row in enumerate(bank):
            f = True
            for j, u in enumerate(row):
                if u == "1": cnt += 1
            if cnt > 0: res += cnt * pre; pre = cnt
            cnt = 0
        return res
# @lc code=end

