import sys
import math
import heapq
import bisect
import numpy as np
from collections import deque, defaultdict, Counter
from typing import List, Optional, Tuple
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        tmp = []
        pack1 = []
        pack2 = []
        def check(u: List[int]) -> bool:
            x = 1
            for t in u:
                x *= t
            return x == target
        def dfs(sta: int) -> bool:
            if sta == n:
                return bool(pack1) and bool(pack2) and check(pack1) and check(pack2)
            pack1.append(nums[sta])
            if dfs(sta + 1):
                return True
            pack1.pop()
            pack2.append(nums[sta])
            if dfs(sta + 1):
                return True
            pack2.pop()
            return False
        
        return dfs(0)