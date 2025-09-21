#
# @lc app=leetcode.cn id=3508 lang=python3
#
# [3508] 设计路由器
#
from mytools import *
# @lc code=start
class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.l = memoryLimit
        self.ss = set()
        self.dt = defaultdict(list)
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        pack = (source, destination, timestamp)
        if pack in self.ss: return False
        if len(self.ss) == self.l: 
            s, d, t = self.q.popleft()
            self.ss.remove((s, d, t))
            idx = bisect_left(self.dt[d], t)
            self.dt[d].pop(idx)
        self.q.append(pack)
        self.ss.add(pack)
        insort(self.dt[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q: return []
        s, d, t = self.q.popleft()
        self.ss.remove((s, d, t))
        idx = bisect_left(self.dt[d], t)
        self.dt[d].pop(idx)
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        t = self.dt.get(destination, [])
        if not t: return 0
        sta = bisect_left(t, startTime)
        eds = bisect_right(t, endTime)
        return eds - sta

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# @lc code=end

