#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

# @lc code=start
class Solution:
    def pushDominoes(self, d: str) -> str:
        d = list('L' + d + 'R')
        n = len(d)
        pre = 0
        for i in range(1, n):
            if d[i] == '.':
                continue
            if d[i] == d[pre]:
                d[pre:i] = d[i] * (i - pre)
            else:
                if d[i] == 'L':
                    m = (pre + i - 1) // 2
                    d[pre:m + 1] = 'R' * (m - pre + 1)
                    m = (pre + i) // 2 + 1
                    d[m:i] = 'L' * (i - m)
            pre = i
        return ''.join(d[1:n - 1])
# @lc code=end

