#
# @lc app=leetcode.cn id=3408 lang=python3
#
# [3408] 设计任务管理器
#
from mytools import *


# @lc code=start
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.mp = {taskId: (priority, userId) for userId, taskId, priority in tasks}
        self.h = [
            (-priority, -taskId, userId) for userId, taskId, priority in tasks
        ]  # 取相反数，变成最大堆
        heapify(self.h)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (priority, userId)
        heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # 懒修改
        self.add(self.mp[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # 懒删除
        self.mp[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heappop(self.h)
            if self.mp[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
            # else 货不对板，堆顶和 mp 中记录的不一样，说明堆顶数据已被修改或删除，不做处理
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# @lc code=end
