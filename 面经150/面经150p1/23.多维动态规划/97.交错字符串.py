#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if len(s3) != n1 + n2: return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(1, n1 + 1):
            if s1[i - 1] != s3[i - 1]: break
            dp[i][0] = True
        for j in range(1, n2 + 1):
            if s2[j - 1] != s3[j - 1]: break
            dp[0][j] = True
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = ((dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) 
                            or (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]))
        return dp[n1][n2]
# @lc code=end


