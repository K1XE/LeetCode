#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from mytools import *
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        n = len(nums)
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] <= i - k: q.popleft()
            if i >= k - 1: res.append(nums[q[0]]) 
        return res
# @lc code=end

