#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#
from mytools import *
# @lc code=start
class Solution:
    def numEquivDominoPairs(self, d: List[List[int]]) -> int:
        cnt = 0
        hash = defaultdict(int)
        for i in range(len(d)):
            u = tuple(d[i])
            if u in hash:
                hash[u] += 1
                continue
            v = tuple([d[i][1], d[i][0]])
            if v in hash:
                hash[v] += 1
                continue
            hash[u] += 1
        for key, val in hash.items():
            cnt += sum(range(1, val))
        return cnt
# @lc code=end

