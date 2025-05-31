#
# @lc app=leetcode.cn id=3362 lang=python3
#
# [3362] 零数组变换 III
#
from mytools import *
# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda q: q[0])
        h = []
        n = len(nums)
        diff = [0] * n
        sums_d = j = 0
        for i, x in enumerate(nums):
            sums_d += diff[i]
            while j < len(queries) and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1
            while sums_d + x > 0 and h and -h[0] >= i:
                sums_d -= 1
                r = -heapq.heappop(h)
                if r + 1 < n:
                    diff[r + 1] += 1
            if sums_d + x > 0: return -1
        return len(h)


# @lc code=end

