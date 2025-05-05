#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#


# @lc code=start
import numpy as np
MOD = 1_000_000_007
class Solution:

    def numTilings(self, n: int) -> int:
        def pow_mul(a: np.ndarray, n: int, f: np.ndarray) -> np.ndarray:
            res = f
            while n:
                if n & 1:
                    res = a @ res % MOD
                a = a @ a % MOD
                n >>= 1
            return res
        if n == 1:
            return 1
        f2 = np.array([2, 1, 1], dtype=object)
        m = np.array([[2, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=object)
        fn = pow_mul(m, n - 2, f2)
        return fn[0]
# @lc code=end

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = (2 * f[i - 1] + f[i - 3]) % MOD
        return f[n]