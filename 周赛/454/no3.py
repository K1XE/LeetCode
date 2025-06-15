import sys
import math
import heapq
import bisect
import numpy as np
from collections import deque, defaultdict, Counter
from itertools import combinations
from typing import List, Optional, Tuple
from functools import cache
from sortedcontainers import SortedSet
dir = (1, 0), (-1, 0), (0, 1), (0, -1)
inf = float('inf')
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        pmax_ = pmin_ = nums[0]
        res = -inf
        n = len(nums)
        for i in range(m - 1, n):
            idx = i - (m - 1)
            pmax_ = max(pmax_, nums[idx])
            pmin_ = min(pmin_, nums[idx])
            res = max(res, pmax_ * nums[i], pmin_ * nums[i])
        return res