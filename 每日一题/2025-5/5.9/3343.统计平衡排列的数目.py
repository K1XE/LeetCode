#
# @lc app=leetcode.cn id=3343 lang=python3
#
# [3343] 统计平衡排列的数目
#
from mytools import *
# @lc code=start
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 1_000_000_007
        cnt = 0
        n = len(num)
        vis = [0] * n
        def check(pack: str):
            odd, even = 0, 0
            for i in range(len(num)):
                if i % 2 == 0:
                    even += int(pack[i])
                else:
                    odd += int(pack[i])
            return even == odd
        def dfs(vis: List, pack: str):
            if len(pack) == n:
                nonlocal cnt
                if check(pack): cnt = (cnt + 1) % MOD
                return
            for i in range(n):
                if vis[i] == 1: continue
                if i > 0 and num[i] == num[i - 1] and vis[i - 1] == 0: continue
                vis[i] = 1
                pack += num[i]
                dfs(vis, pack)
                pack = pack[:-1]
                vis[i] = 0
        num = ''.join(sorted(num))
        dfs(vis, '')
        return cnt
                    

# @lc code=end

