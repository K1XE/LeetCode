#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
from mytools import *
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def check(pack:List):
            for i in range(len(pack)):
                x = int(pack[i])
                if x > 255: return False
                if len(pack[i]) > 1 and pack[i][0] == '0': return False
            return True
        
        def dfs(sta, pack:List, res:List):
            if len(pack) == 4:
                if sta == len(s) and check(pack):
                    u = '.'.join(pack)
                    res.append(u)
                return
            for i in range(sta, min(len(s), sta + 3)):
                sub = s[sta:i + 1]
                pack.append(sub)
                dfs(i + 1, pack, res)
                pack.pop()
        res = []
        dfs(0, [], res)
        return res
# @lc code=end

