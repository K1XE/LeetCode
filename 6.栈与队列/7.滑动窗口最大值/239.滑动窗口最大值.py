#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
from collections import deque
import heapq

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i in range(len(nums)) :
            while q and nums[q[-1]] < nums[i] :
                q.pop()
            q.append(i)
            if (i - q[0] + 1 > k) :
                q.popleft()
            if (i + 1 >= k) :
                res.append(nums[q[0]])
        return res



# @lc code=end

class Solution:
    def __init__(self):
        self.q = deque()
    def pop(self, x):
        if self.q and self.q[0] == x :
            self.q.popleft()
    def push(self, x):
        while self.q and self.q[-1] < x :
            self.q.pop()
        self.q.append(x)    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(k) :
            self.push(nums[i])
        res.append(self.q[0])
        for i in range(k, len(nums)) :
            self.pop(nums[i - k])
            self.push(nums[i])
            res.append(self.q[0])
        return res



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap : List[tuple[int, int]] = []
        res : List[int] = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while (i - heap[0][1] + 1> k):
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res