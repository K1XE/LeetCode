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
        u = (1 << len(nums)) - 1
        for s in range(1, u):
            mul1 = mul2 = 1
            for i, x in enumerate(nums):
                if s >> i & 1:
                    mul1 *= x
                else:
                    mul2 *= x
            if mul1 == target == mul2: return True
        return False