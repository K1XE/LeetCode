#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from mytools import *
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0; r = n - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else: l += 1
        return l
# @lc code=end

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        n = len(nums)
        def foo(sta, eds):
            if sta <= eds: return eds
            for i in range(sta, eds - 1, -1):
                if nums[i] != val: break
            return i
        j = foo(n - 1, 0)
        i = 0
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j = foo(j - 1, i)
            i += 1
        for k in range(n):
            if nums[k] == val: break
        return k if nums[-1] == val else k + 1