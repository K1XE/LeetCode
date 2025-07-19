#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0; r = len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target: return [l + 1, r + 1]
            elif cur > target: r -= 1
            else: l += 1
# @lc code=end

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            tar = target - numbers[i]
            l = i + 1; r = n - 1
            while l <= r:
                mid = l + r >> 1
                if numbers[mid] == tar: return [i + 1, mid + 1]
                elif numbers[mid] < tar: l = mid + 1
                else: r = mid - 1
        