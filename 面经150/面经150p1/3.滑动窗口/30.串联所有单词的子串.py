#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from mytools import *
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hash = defaultdict(int)
        for st in words: hash[st] += 1
        sz1 = len(words); sz2 = len(words[0])
        sz = sz1 * sz2
        n = len(s)
        res = []
        for offset in range(sz2):
            i = offset
            while i + sz <= n:
                if i == offset:
                    tmp = defaultdict(int)
                    j = i
                    while j < i + sz:
                        tmp[s[j:j + sz2]] += 1
                        j += sz2
                else:
                    l = s[i - sz2:i]
                    tmp[l] -= 1
                    if tmp[l] == 0: del tmp[l]
                    nw = s[i + sz - sz2:i + sz]
                    tmp[nw] += 1
                if tmp == hash: res.append(i)
                i += sz2
        return res
# @lc code=end

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hash = defaultdict(int)
        for st in words: hash[st] += 1
        sz1 = len(words); sz2 = len(words[0])
        sz = sz1 * sz2
        n = len(s)
        res = []
        i = j = 0
        while i < n:
            tmp = defaultdict(int)
            if i + sz > n: break
            j = i
            while j < i + sz:
                s1 = ""
                s1 = s[j:j + sz2]
                tmp[s1] += 1
                j += sz2
            if hash == tmp: res.append(i)
            i += 1
        return res
            