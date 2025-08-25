#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from mytools import *
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(x) for x in nums]
        def cmp(a, b):
            if a + b == b + a: return 0
            elif a + b > b + a: return -1
            else: return 1
        s.sort(key=cmp_to_key(cmp))
        return ''.join(s) if s[0] != '0' else '0'
# @lc code=end

