#
# @lc app=leetcode.cn id=3403 lang=python3
#
# [3403] 从盒子中找出字典序最大的字符串 I
#
from mytools import *
# @lc code=start
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        n = len(word)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and word[i + k] == word[j + k]:
                k += 1
            if j + k < n and word[i + k] < word[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else: j += k + 1
        return word[i : i + n - numFriends + 1]
# @lc code=end

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        res = ""
        for cnt in combinations(range(1, n), numFriends - 1):
            cnt = [0] + list(cnt) + [n]
            for i in range(len(cnt) - 1):
                sub = word[cnt[i]:cnt[i + 1]]
                if sub > res: res = sub
        return res
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        len_ = len(word) - (numFriends - 1)
        maxidx, maxch = -1, 'a'
        for i, ch in enumerate(word):
            if ch >= maxch:
                maxidx = i
                maxch = ch
        pack = []
        for i, ch in enumerate(word):
            if ch == maxch:
                pack.append(i)
        res = ["" for _ in range(len(pack))]
        for i, idx in enumerate(pack):
            for j in range(idx, idx + len_):
                if j < len(word):
                    res[i] += word[j]
        res.sort(reverse=True)
        return res[0]
        