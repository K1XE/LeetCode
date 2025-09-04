#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        sz = len(num) - k
        for d in num:
            while k and stk and stk[-1] > d: stk.pop(); k -= 1
            stk.append(d)
        return ''.join(stk[:sz]).lstrip('0') or '0'
# @lc code=end

