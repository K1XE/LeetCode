#
# @lc app=leetcode.cn id=3307 lang=python3
#
# [3307] 找出第 K 个字符 II
#
from mytools import *
# @lc code=start
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lens = [1]
        for op in operations:
            lens.append(lens[-1] * 2)
        shift_cnt = 0
        idx = len(operations)
        while idx > 0:
            pre_len = lens[idx - 1]
            op = operations[idx - 1]
            if k > pre_len:
                k -= pre_len
                if op == 1:
                    shift_cnt += 1
            idx -= 1
        ch = 'a'
        for _ in range(shift_cnt):
            ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
        return ch

# @lc code=end

