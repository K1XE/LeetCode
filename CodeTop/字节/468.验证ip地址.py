#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#
from mytools import *
# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isv4(a: List):
            if len(a) != 4: return False
            def ck(sub: str):
                if len(sub) > 1 and sub[0] == "0": return False
                if not sub.isdigit() or int(sub) > 255 or int(sub) < 0: return False
                return True
            for sub in a:
                if not ck(sub): return False
            return True
        def isv6(a: List):
            if len(a) != 8: return False
            def ck(sub: str):
                if len(sub) > 4 or len(sub) == 0: return False
                for ch in sub:
                    if 'f' < ch <= 'z' or 'F' < ch <= 'Z': return False
                return True
            for sub in a:
                if not ck(sub): return False
            return True
        if isv4(queryIP.split(".")): return "IPv4"
        elif isv6(queryIP.split(":")): return "IPv6"
        else: return "Neither"
# @lc code=end

