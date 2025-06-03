#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
from mytools import *
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        a = 0; b = 1; c = 0
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c
        return c
# @lc code=end

class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n <= 1: return n
            return f(n - 1) + f(n - 2)
        return f(n)