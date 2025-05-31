#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#
from mytools import *
# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        for j in range(len(arr)):
            if arr[j] % 2 != 1:
                i = j + 1
                continue
            if j - i + 1 >= 3: return True
        return False
# @lc code=end

