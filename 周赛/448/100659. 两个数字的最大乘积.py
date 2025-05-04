from mytools import *

class Solution:
    def maxProduct(self, n: int) -> int:
        tmp = []
        def get_num(n):
            while n:
                u = n % 10
                nonlocal tmp
                tmp.append(u)
                n //= 10
            return
        get_num(n)
        a = max(tmp)
        tmp.remove(a)
        b = max(tmp)
        return a*b


