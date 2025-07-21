#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = defaultdict(int)
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x in hash:
                if abs(i - hash[x]) <= k: return True
            hash[x] = i
        return False
# @lc code=end

