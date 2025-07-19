#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
from mytools import *
# @lc code=start
class RandomizedSet:
    def __init__(self):
        self.idx = defaultdict(int)
        self.data = []
    def insert(self, val: int) -> bool:
        if val in self.idx: return False
        self.idx[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx: return False
        last = self.data[-1]
        i = self.idx[val]
        self.data[i] = last
        self.idx[last] = i
        self.idx.pop(val)
        self.data.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

class RandomizedSet:
    def __init__(self):
        self.ss = set()
    def insert(self, val: int) -> bool:
        if val in self.ss: return False
        else: self.ss.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ss: return False
        else: self.ss.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.ss))

