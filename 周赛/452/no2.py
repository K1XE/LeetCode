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
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        def calc(x1, x2, y1, y2):
            tmp = []
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    tmp.append(grid[i][j])
            tmp = sorted(set(tmp))
            if len(tmp) <= 1: return 0
            ans = float('inf')
            for i in range(1, len(tmp)):
                d = tmp[i] - tmp[i - 1]
                if ans > d: ans = d
            return ans
        i, j = 0, 0
        x1, x2 = i, j
        while x1 < m - k + 1:
            y1 = 0
            while y1 < n - k + 1:
                x2, y2 = x1 + k - 1, y1 + k - 1
                res[x1][y1] = calc(x1, x2, y1, y2)
                y1 += 1
            x1 += 1
        return res