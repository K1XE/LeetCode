import sys
import math
import heapq
import bisect
import numpy as np
from collections import deque, defaultdict, Counter
from typing import List, Optional, Tuple
from functools import cache
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