#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from mytools import *
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palin = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 3 or is_palin[i + 1][j - 1]):
                    is_palin[i][j] = True
        def dfs(sta, pack: List, res: List):
            if sta == n:
                res.append(pack.copy())
                return
            for eds in range(sta, n):
                sub = s[sta:eds + 1]
                if is_palin[sta][eds]:
                    pack.append(sub)
                    dfs(eds + 1, pack, res)
                    pack.pop()
        res = []
        dfs(0, [], res)
        return res

# @lc code=end

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(sta, pack: List, res: List):
            if sta == len(s):
                res.append(pack.copy())
                return
            for i in range(sta, len(s)):
                sub = s[sta:i + 1]
                if sub != sub[::-1]:
                    continue
                pack.append(sub)
                dfs(i + 1, pack, res)
                pack.pop()
        res = []
        dfs(0, [], res)
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palin(s: str):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        
        def check(pack: List):
            for s in pack:
                if not palin(s): return False
            return True

        def dfs(sta, pack: List, res: List, _len):
            if _len == len(s):
                if check(pack): res.append(pack.copy())
                return
            for i in range(sta, len(s)):
                pack.append(s[sta:i + 1])
                _len += i + 1 - sta
                dfs(i + 1, pack, res, _len)
                _len -= i + 1 - sta
                pack.pop()
        res = []
        dfs(0, [], res, 0)
        return res