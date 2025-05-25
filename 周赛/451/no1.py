from mytools import *
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k: return 0
        c = 0
        minv = float('inf')
        if n > k:
            for i in range(1, k + 1):
                x1 = i
                x2 = n - i
                if x2 > k: continue
                minv = min(minv, x1 * x2)
            c += minv
        minv = float('inf')
        if m > k:
            for i in range(1, k + 1):
                x1 = i
                x2 = m - i
                if x2 > k: continue
                minv = min(minv, x1 * x2)
            c += minv
        return c