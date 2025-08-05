#
# @lc app=leetcode.cn id=3477 lang=python3
#
# [3477] 水果成篮 II
#
from mytools import *
# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        res = 0
        for i in range(n):
            f = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    f = True
                    used[j] = True
                    break
            if not f: res += 1
        return res

# @lc code=end

