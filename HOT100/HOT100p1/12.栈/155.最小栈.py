#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
from mytools import *
# @lc code=start
class MinStack:

    def __init__(self):
        self.stk = [(0, float('inf'))]

    def push(self, val: int) -> None:
        self.stk.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

