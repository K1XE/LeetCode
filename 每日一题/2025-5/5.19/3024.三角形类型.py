#
# @lc app=leetcode.cn id=3024 lang=python3
#
# [3024] 三角形类型
#
from mytools import *
# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        def check(a, b, c):
            return (a + b <= c) or (a + c <= b) or (b + c <= a)
        a, b, c = nums[0], nums[1], nums[2]
        if check(a, b, c): return "none"
        if a == b == c: return "equilateral"
        if a == b or b == c or a == c: return "isosceles"
        return "scalene"
# @lc code=end

