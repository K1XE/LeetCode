#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        nxt_nums = 0
        cur_str = ''
        stk = []
        for ch in s:
            if ch.isdigit():
                nxt_nums = nxt_nums * 10 + int(ch)
            elif ch == '[':
                stk.append((cur_str, nxt_nums))
                cur_str = ''
                nxt_nums = 0
            elif ch == ']':
                last_str, cur_nums = stk.pop()
                cur_str = last_str + cur_str * cur_nums
            else:
                cur_str += ch
        return cur_str
# @lc code=end

