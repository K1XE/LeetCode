#
# @lc app=leetcode.cn id=3337 lang=python3
#
# [3337] 字符串转换后的长度 II
#
from mytools import *
# @lc code=start
class Solution:
    
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1_000_000_007
        def matmul(a: List[List], b: List[List]):
            return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(* b)] for row in a]
        
        def pow_mul(a, n, f0):
            res = f0
            while n:
                if n & 1:
                    res = matmul(a, res)
                a = matmul(a, a)
                n >>= 1
            return res
        
        f0 = [[1] for _ in range(26)]
        m = [[0] * 26 for _ in range(26)]
        for i, cnt in enumerate(nums):
            for j in range(i + 1, i + cnt + 1):
                m[i][j % 26] = 1
        
        mt = pow_mul(m, t, f0)
        res = 0
        for ch, cnt in Counter(s).items():
            res += mt[ord(ch) - ord('a')][0] * cnt
        return res % MOD


# @lc code=end

