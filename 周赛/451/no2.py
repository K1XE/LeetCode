from mytools import *
class Solution:
    def resultingString(self, s: str) -> str:
        cur = 1
        n = len(s)
        while cur < n:
            if s[cur - 1] == s[cur]:
                