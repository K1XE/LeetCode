#
# @lc app=leetcode.cn id=2014 lang=python3
#
# [2014] 重复 K 次的最长子序列
#
from mytools import *
# @lc code=start
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        hot = ''.join(ele * (cnt[ele] // k) for ele in sorted(cnt, reverse=True))
        for i in range(len(hot), 0, -1):
            for item in permutations(hot, i):
                word = ''.join(item)
                ss = iter(s)
                if all(c in ss for c in word * k): return word
        return ''
# @lc code=end

