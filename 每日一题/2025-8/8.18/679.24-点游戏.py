#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
from typing import List
# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(pack):
            if len(pack) == 1: return abs(pack[0] - 24) < 1e-6
            for i in range(len(pack)):
                for j in range(i + 1, len(pack)):
                    n1 = pack[i]
                    n2 = pack[j]
                    tmp = [pack[k] for k in range(len(pack)) if k != i and k != j]
                    cur = [n1 + n2, n1 - n2, n2 - n1, n1 * n2]
                    if abs(n1) > 1e-6: cur.append(n2 / n1)
                    if abs(n2) > 1e-6: cur.append(n1 / n2)
                    for val in cur:
                        if dfs(tmp + [val]): return True
            return False
        return dfs(cards)
# @lc code=end

