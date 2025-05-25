#include "tools.h"
class Solution
{
public:
    using ll = long long;
    const int MOD = 1e9 + 7;
    ll mypow(ll a, ll e)
    {
        ll r = 1;
        while (e > 0)
        {
            if (e & 1)
                r = (r * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return r;
    }

    int assignEdgeWeights(vector<vector<int>> &edges)
    {
        int n = edges.size() + 1;
        vector<vector<int>> g(n + 1);
        for (auto &e : edges)
        {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }

        int L = 0;
        auto dfs = [&](auto &&self, int u, int parent, int d) -> void
        {
            L = max(L, d);
            for (int v : g[u])
            {
                if (v == parent)
                    continue;
                self(self, v, u, d + 1);
            }
        };
        dfs(dfs, 1, 0, 0);
        return (int)mypow(2, L - 1);
    }
};
