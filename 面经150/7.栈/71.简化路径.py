#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        n = len(path)
        res = ""
        i = 0
        while i < n:
            if path[i] == '/': i += 1; continue
            s = ""
            while i < n and path[i] != '/': s += path[i]; i += 1
            if s == "..":
                if stk: stk.pop()
                else: continue
            elif s != ".": stk.append(s)
        for s in stk: res += '/' + s
        return res if res != "" else "/"
# @lc code=end

