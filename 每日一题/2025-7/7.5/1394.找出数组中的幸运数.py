#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#
from mytools import *
# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash = defaultdict(int)
        for x in arr:
            hash[x] += 1
        res = -1
        for key, val in hash.items():
            if key == val:
                res = max(res, key)
        return res
# @lc code=end

