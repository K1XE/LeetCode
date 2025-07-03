#
# @lc app=leetcode.cn id=3304 lang=python3
#
# [3304] 找出第 K 个字符 I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        def get_char(k):
            if k == 1: return 'a'
            prev = get_char((k + 1) // 2)
            return chr((ord(prev) - ord('a') + (k + 1) % 2) % 26 + ord('a'))
        return get_char(k)
# @lc code=end
class Solution:
    def kthCharacter(self, k: int) -> str:
        def get_nxt(c):
            return chr((ord(c) - ord("a") + 1) % 26 + ord("a"))
        word = ["a"]
        while len(word) < k:
            for i in range(len(word)):
                word.append(get_nxt(word[i]))
        return word[k - 1] 
