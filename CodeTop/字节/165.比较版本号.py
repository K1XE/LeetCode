#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#
from mytools import *
# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for a, b in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            x, y = int(a), int(b)
            if x != y:
                return 1 if x > y else 0
        return 0
            
# @lc code=end

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        m, n = len(version1), len(version2)
        
        while i < m and j < n:
            s1, s2 = "", ""
            while i < m and version1[i] != '.':
                s1 += version1[i]
                i += 1
            while j < n and version2[j] != '.':
                s2 += version2[j]
                j += 1
            if int(s1) > int(s2): return 1
            elif int(s1) < int(s2): return -1
            i += 1; j += 1

        if i >= m:
            for u in range(j, n):
                if version2[u] != '.' and version2[u] != '0': return -1
        else:
            for u in range(i, m):
                if version1[u] != '.' and version1[u] != '0': return 1
        return 0