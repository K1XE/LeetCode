#
# @lc app=leetcode.cn id=3005 lang=python3
#
# [3005] 最大频率元素计数
#
from mytools import *
# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for x in nums:
            hash[x] += 1
        print(hash)
        ret = defaultdict(int)
        for _, v in hash.items():
            ret[v] += 1
        print(ret)
        maxk = 0
        for k, v in ret.items():
            if k >= maxk: maxk = k
        for k, v in ret.items():
            if k == maxk: return k * v
# @lc code=end

