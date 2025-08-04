#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
from collections import defaultdict
from typing import *
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash = defaultdict(int)
        n = len(fruits); j = 0
        s = 0
        res = 0
        for i in range(n):
            hash[fruits[i]] += 1
            s += 1
            while len(hash) > 2:
                s -= 1
                hash[fruits[j]] -= 1
                if hash[fruits[j]] == 0: hash.pop(fruits[j])
                j += 1
            res = max(res, s)
        return res

# @lc code=end

