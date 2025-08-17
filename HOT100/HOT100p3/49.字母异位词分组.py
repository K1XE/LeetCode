#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tmp = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                tmp[idx] += 1
            res[''.join(str(tmp))].append(s)
        re = []
        for k, v in res.items():
            re.append(v)
        return re
# @lc code=end

