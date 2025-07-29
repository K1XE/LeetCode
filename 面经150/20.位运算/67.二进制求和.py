#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1, l2 = len(a) - 1, len(b) - 1
        s = 0
        res = []
        while l1 >= 0 or l2 >= 0 or s:
            if l1 >= 0:
                s += int(a[l1])
                l1 -= 1
            if l2 >= 0:
                s += int(b[l2])
                l2 -= 1
            res.append(str(s % 2))
            s //= 2
        res.reverse()
        return ''.join(res)
# @lc code=end

