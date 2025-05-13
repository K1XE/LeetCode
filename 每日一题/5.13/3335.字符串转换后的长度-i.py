#
# @lc app=leetcode.cn id=3335 lang=python3
#
# [3335] 字符串转换后的长度 I
#
from mytools import *
# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cur = [0] * 26
        MOD = 1_000_000_007
        
        for ch in s:
            cur[ord(ch) - ord('a')] += 1
        
        for _ in range(t):
            nxt_state = [0] * 26
            nxt_state[0] = cur[25]
            nxt_state[1] = (cur[0] + cur[25]) % MOD
            for i in range(2, 26):
                nxt_state[i] = cur[i - 1]
            cur = nxt_state
        return sum(cur) % MOD
# @lc code=end

