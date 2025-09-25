#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
from mytools import *
# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator); denominator = abs(denominator)
        q, r = divmod(numerator, denominator)
        if r == 0: return sign + str(q)
        res = [sign + str(q) + "."]
        hash = {r : 1}
        while r:
            q, r = divmod(r * 10, denominator)
            res.append(str(q))
            if r in hash:
                pos = hash[r]
                return f"{''.join(res[:pos])}({''.join(res[pos:])})"
            hash[r] = len(res)
        return ''.join(res)
        
# @lc code=end

