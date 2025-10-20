#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#
from mytools import *
# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1] == "+" else -1 for op in operations)
    
# @lc code=end

