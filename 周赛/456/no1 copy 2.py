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
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def get_back(w1, w2):
            l = min(len(w1), len(w2))
            idx = 0
            while idx < l and w1[idx] == w2[idx]: idx += 1
            return idx
        n = len(words)
        back = [get_back(words[i], words[i + 1]) for i in range(n - 1)]
        pre = [0] * (n - 1)
        pre[0] = back[0]
        for i in range(1, n - 1): pre[i] = max(pre[i - 1], back[i])
        suf = [0] * (n - 1)
        suf[-1] = back[-1]
        for i in range(n - 3, -1, -1): suf[i] = max(suf[i + 1], back[i])
        res = [0] * n
        for i in range(n):
            maxl = 0
            if i - 2 >= 0: maxl = max(maxl, pre[i - 2])
            if i + 1 <= n - 2: maxl = max(maxl, suf[i + 1])
            if 0 < i < n - 1:
                maxl = max(maxl, get_back(words[i - 1], words[i + 1]))
            res[i] = maxl
        return res