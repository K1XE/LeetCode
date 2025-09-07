#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = (rand7() - 1) * 7 + rand7()
        while True:
            x = (rand7() - 1) * 7 + rand7()
            if x <= 40: return x % 10 + 1
            a = x - 40
            x = (a - 1) * 7 + rand7()
            if x <= 60: return x % 10 + 1
            a = x - 60
            x = (a - 1) * 7 + rand7()
            if x <= 20: return x % 10 + 1
            
# @lc code=end

