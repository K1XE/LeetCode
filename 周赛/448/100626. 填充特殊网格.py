from mytools import *
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        size = 1<<N
        u = 0
        res = [[0] * size for i in range(size)]
        def dfs(l, r, t, b):
            if r - l == 1:
                nonlocal u
                res[t][l] = u
                u += 1
                return
            m = (r - l) // 2
            dfs(l + m, r, t, t + m)
            dfs(l + m, r, t + m, b)
            dfs(l, l + m, t + m, b)
            dfs(l, l + m, t, t + m)
        dfs(0, size, 0, size)
        return res


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        size = 2**N
        sta = 0
        eds = 2**(2*N) - 1
        res = [[0]*size for i in range(size)]
        def dfs(g, x, y, size, sta, eds):
            if size==1:
                g[x][y] = sta
                return
            tmp = size//2
            four = (eds - sta + 1)//4
            dfs(g, x, y + tmp, tmp, sta, sta + four - 1)
            dfs(g, x + tmp, y + tmp, tmp, sta + four, sta + 2 * four - 1)
            dfs(g, x + tmp, y, tmp, sta + 2 * four, sta + 3 * four - 1)
            dfs(g, x, y, tmp, sta + 3 * four, eds)
        dfs(res, 0, 0, size, sta, eds)
        return res
