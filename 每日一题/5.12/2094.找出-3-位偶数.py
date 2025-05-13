#
# @lc app=leetcode.cn id=2094 lang=python3
#
# [2094] 找出 3 位偶数
#
from mytools import *
# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        vis = [0] * n
        def check(pack: List):
            if pack[-1] % 2 == 0 and pack[0] != 0: return True
            return False
        def solve(pack: List):
            return pack[0] * 100 + pack[1] * 10 + pack[2]
        
        def dfs(vis, res: List, pack: List):
            if (len(pack) == 3):
                if check(pack):
                    res.append(solve(pack))
                return
            for i in range(n):
                if vis[i] == 1: continue
                if i > 0 and digits[i] == digits[i - 1] and vis[i - 1] == 0: continue
                pack.append(digits[i])
                vis[i] = 1
                dfs(vis, res, pack)
                vis[i] = 0
                pack.pop()
        res = []
        digits.sort()
        dfs(vis, res, [])
        return res
# @lc code=end

