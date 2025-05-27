#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        def cntHash():
            hash = [[float('-inf')] * 2 for _ in range(26)]
            hash_f = []
            for i in range(n):
                if hash[ord(s[i]) - ord('a')][0] == float("-inf"):
                    hash[ord(s[i]) - ord('a')][0] = i
                hash[ord(s[i]) - ord('a')][1] = i
            for u in hash:
                if u[0] != float("-inf"):
                    hash_f.append(u)
            return hash_f
        hash = cntHash()
        hash.sort(key=lambda x: (x[0], x[1]))
        end = hash[0][1]
        start = 0
        res = []
        for i in range(1, len(hash)):
            if hash[i][0] > end:
                res.append(end - start + 1)
                start = end + 1
            end = max(end, hash[i][1])
        res.append(end - start + 1)
        return res
# @lc code=end

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {ch : i for i, ch in enumerate(s)}
        start, end = 0, 0
        n = len(s)
        res = []
        for i in range(n):
            end = max(end, hash[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res