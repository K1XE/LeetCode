#
# @lc app=leetcode.cn id=3443 lang=python3
#
# [3443] K 次修改后的最大曼哈顿距离
#

# @lc code=start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        x = y = 0
        res = 0
        for i, c in enumerate(s, start=1):
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            tmp = min(i, abs(x) + abs(y) + 2 * k)
            res = max(res, tmp)
        return res
# @lc code=end

