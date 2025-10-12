#
# @lc app=leetcode.cn id=3539 lang=python3
#
# [3539] 魔法序列的数组乘积之和
#
from mytools import *

# @lc code=start
MOD = 1_000_000_007
MX = 31

fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD
inv_f = [0] * MX
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        pow_v = [[1] * (m + 1) for _ in range(n)]
        for i, v in enumerate(nums):
            for j in range(1, m + 1):
                pow_v[i][j] = pow_v[i][j - 1] * v % MOD

        @cache
        def dfs(i: int, left_m: int, x: int, left_k: int) -> int:
            c1 = x.bit_count()
            if c1 + left_m < left_k:  # 可行性剪枝
                return 0
            if i == n or left_m == 0 or left_k == 0:  # 无法继续选数字
                return 1 if left_m == 0 and c1 == left_k else 0
            res = 0
            for j in range(left_m + 1):  # 枚举 I 中有 j 个下标 i
                # 这 j 个下标 i 对 S 的贡献是 j * pow(2, i)
                # 由于 x = S >> i，转化成对 x 的贡献是 j
                bit = (x + j) & 1  # 取最低位，提前从 left_k 中减去，其余进位到 x 中
                r = dfs(i + 1, left_m - j, (x + j) >> 1, left_k - bit)
                res += r * pow_v[i][j] * inv_f[j]
            return res % MOD

        return dfs(0, m, 0, k) * fac[m] % MOD


# @lc code=end
