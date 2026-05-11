#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
from mytools import *
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.h = defaultdict(int)
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.h: return False
        self.h[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h: return False
        idx = self.h[val]
        lxt = self.data[-1]
        self.data[idx] = lxt
        self.h[lxt] = idx
        self.h.pop(val)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

