#
# @lc app=leetcode.cn id=1912 lang=python3
#
# [1912] 设计电影租借系统
#
from mytools import *
# @lc code=start
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.sm2p = {}
        self.urm2ps = defaultdict(SortedList)
        self.rm = SortedList()
        
        for s, m, p in entries:
            self.sm2p[(s, m)] = p
            self.urm2ps[m].add((p, s))

    def search(self, movie: int) -> List[int]:
        return [s for _, s in self.urm2ps[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.sm2p[(shop, movie)]
        self.urm2ps[movie].discard((p, shop))
        self.rm.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.sm2p[(shop, movie)]
        self.rm.discard((p, shop, movie))
        self.urm2ps[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return [[s, m] for _, s, m in self.rm[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @lc code=end

