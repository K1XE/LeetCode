#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from mytools import *
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        s = 0
        res = 0
        for x in nums:
            s += x
            res += hash[s - k]
            hash[s] += 1
            
        return res
# @lc code=end

