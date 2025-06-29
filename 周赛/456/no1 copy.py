import sys
import math
import heapq
import random
import bisect
import numpy as np
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations
from typing import List, Optional, Tuple
from functools import cache
from sortedcontainers import SortedSet, SortedDict
dir = (1, 0), (-1, 0), (0, 1), (0, -1)
inf = float('inf')
# 二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        px = [0] * (n + 1)
        for i in range(n):
            px[i + 1] = px[i] ^ nums[i]
        def cost(i: int, j: int) -> int:
            return px[j] ^ px[i]
        INF = 10**18
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        for j in range(1, n + 1):
            dp[1][j] = cost(0, j)
        for m in range(2, k + 1):
            for j in range(m, n + 1):
                best = INF
                for i in range(m - 1, j):
                    val = max(dp[m - 1][i], cost(i, j))
                    if val < best:
                        best = val
                dp[m][j] = best
        return dp[k][n]
