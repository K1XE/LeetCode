#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
from collections import defaultdict
from random import choice
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.hash = defaultdict(int)
        self.data = []
    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        self.hash[val] = len(self.data)
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hash: return False
        lxt = self.data[-1]
        i = self.hash[val]
        self.data[i] = lxt
        self.hash[lxt] = i
        self.hash.pop(val)
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

