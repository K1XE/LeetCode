#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
from mytools import *
# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tmp1 = tmp2 = 0
        p1 = p2 = 0
        for x in reversed(arr1): tmp1 += (-2) ** p1 if x == 1 else 0; p1 += 1
        for x in reversed(arr2): tmp2 += (-2) ** p2 if x == 1 else 0; p2 += 1
        s = tmp1 + tmp2
        if s == 0: return [0]
        res = []
        while s != 0:
            s,r = divmod(s, -2)
            if r < 0:
                r += 2
                s += 1
            res.append(r)
        return res[::-1]
        
# @lc code=end

