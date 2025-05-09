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
                v = g[u].pop()
                dfs(v)
            res.append(u)
        dfs("JFK")
        return res[::-1]



# @lc code=end

# TLE
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets) + 1
        def dfs(vis, pack: List, res: List):
            if len(pack) == n:
                if res == [] or res > pack:
                    res.clear()
                    res.extend(pack)
                return
            for i in range(len(tickets)):
                if tickets[i][0] != pack[-1] or vis[i] == 1: continue
                pack.append(tickets[i][1])
                vis[i] = 1
                dfs(vis, pack, res)
                pack.pop()
                vis[i] = 0
        res = []
        vis = [0] * n
        dfs(vis, ["JFK"], res)
        return res