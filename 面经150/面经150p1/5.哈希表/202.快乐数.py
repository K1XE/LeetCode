#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        ss = set()
        while n != 1:
            tmp = str(n)
            x = 0
            for c in tmp:
                x += int(c) ** 2
            n = x
            if n in ss: return False
            else: ss.add(n)
        return True
# @lc code=end
class Solution:
    def isHappy(self, n: int) -> bool:
        ss = set()
        while n != 1:
            tmp = str(n)
            x = 0
            p = len(tmp) - 1
            cnt = [0] * 10
            for c in tmp:
                cnt[ord(c) - ord('0')] += 1
                x += int(c) ** 2
                p -= 1
            n = x
            if tuple(cnt) in ss: return False
            else: ss.add(tuple(cnt))
        return True
