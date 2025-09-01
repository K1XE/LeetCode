#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#
from mytools import *
# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [((a - b) / (b * (b + 1)), a, b) for a, b in classes]
        heapify(h)
        for _ in range(extraStudents):
            _, a, b = h[0]
            a += 1; b += 1
            heapreplace(h, ((a - b) / (b * (b + 1)), a, b))
        return sum(a / b for _, a, b in h)/ len(h)
# @lc code=end

