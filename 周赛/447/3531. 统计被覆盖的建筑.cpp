#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        const int INF = 1e9;
        int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
            vector<int> l(n + 1, INF), r(n + 1, -INF), t(n + 1, INF), b(n + 1, -INF);
            int res = 0;
            for (int i = 0; i < buildings.size(); i ++ )
            {
                int u = buildings[i][0], v = buildings[i][1];
                l[u] = min(l[u], v);
                r[u] = max(r[u], v);
                t[v] = min(t[v], u);
                b[v] = max(b[v], u);
            }
            for (int i = 0; i < buildings.size(); i ++ )
            {
                int u = buildings[i][0], v = buildings[i][1];
                if (v > l[u] && v < r[u] && u > t[v] && u < b[v]) res ++;
            }
            return res;
        }

    };