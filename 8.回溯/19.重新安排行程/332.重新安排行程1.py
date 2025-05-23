#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from mytools import *
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for frm, to in tickets:
            g[frm].append(to)
        for frm in g:
            g[frm].sort(reverse=True)
        res = []
        def dfs(u):
            while g[u]:
                tmp = g[u].pop()
                dfs(tmp)
            res.append(u)
        dfs("JFK")
        return res[::-1]
# @lc code=end

