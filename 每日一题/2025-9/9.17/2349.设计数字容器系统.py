#
# @lc app=leetcode.cn id=2349 lang=python3
#
# [2349] 设计数字容器系统
#
from mytools import *
# @lc code=start
class NumberContainers:

    def __init__(self):
        self.idx = {}
        self.nums = defaultdict(SortedSet)
    def change(self, index: int, number: int) -> None:
        x = self.idx.get(index, None)
        if x is not None:
            self.nums[x].discard(index)
        self.idx[index] = number
        self.nums[number].add(index)

    def find(self, number: int) -> int:
        i = self.nums[number]
        return i[0] if i else -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

