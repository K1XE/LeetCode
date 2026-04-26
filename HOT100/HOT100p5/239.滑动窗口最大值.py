#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from mytools import *
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= nums[i]: q.pop()
            q.append(i)
            if i - q[0] + 1 > k: q.popleft()
            if i >= k - 1: res.append(nums[q[0]])
        return res
# @lc code=end

