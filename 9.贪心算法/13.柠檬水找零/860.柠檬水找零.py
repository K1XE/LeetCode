#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
from mytools import *
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for b in bills:
            if b == 5: five += 1
            if b == 10:
                if five <= 0: return False
                else:
                    five -= 1
                    ten += 1
            if b == 20:
                if ten <= 0:
                    if five < 3: return False
                    else:
                        five -= 3
                        twenty += 1
                else:
                    if five < 1: return False
                    else:
                        five -= 1
                        ten -= 1
                        twenty += 1
        return True
            
# @lc code=end

