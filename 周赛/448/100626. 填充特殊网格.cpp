#include <bits/stdc++.h>
using namespace std;
class Solution {
    public:
        vector<vector<int>> specialGrid(int N) {
            int size = pow(2, N);
            vector<vector<int>> res(size, vector<int>(size));
            dfs(res, 0, 0, size, 0, pow(2, 2 * N) - 1);
            return res;
        }
        void dfs(vector<vector<int>>& g, int x, int y, int size, int sta, int eds)
        {
            if (size == 1)
            {
                g[x][y] = sta;
                return;
            }
            int tmp = size / 2;
            int four = (eds - sta + 1) / 4;
            dfs(g, x, y + tmp, tmp, sta, sta + four - 1);
            dfs(g, x + tmp, y + tmp, tmp, sta + four, sta + 2 * four - 1);
            dfs(g, x + tmp, y, tmp, sta + 2 * four, sta + 3 * four - 1);
            dfs(g, x, y, tmp, sta + 3 * four, eds);
        }
};