#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from mytools import *
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def dfs(pack, k):
            l = []; m = []; r = []
            piv = random.choice(pack)
            for x in pack:
                if x < piv:
                    l.append(x)
                elif x == piv:
                    m.append(x)
                else:
                    r.append(x)
            if len(r) >= k:
                return dfs(r, k)
            elif len(r) + len(m) < k:
                return dfs(l, k - (len(r) + len(m)))
            else: return piv
        return dfs(nums, k)
# @lc code=end

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        n = len(nums)
        for i in range(n):
            if len(h) < k: heapq.heappush(h, nums[i])
            else: heapq.heappushpop(h, nums[i])
        return h[0]