#include <bits/stdc++.h>
#include <ranges>
using namespace std;

class Solution {
    public:
        const int MOD = 1'000'000'007;
        vector<int> baseUnitConversions(vector<vector<int>>& conversions) {
            int lease = 1;
            vector<int> t(conversions.size() + 1);
            t[0] = 1;
            do
            {
                lease = 0;
                for (auto pack: conversions)
                {
                    int src = pack[0], tar = pack[1];
                    long long f = pack[2];
                    if (t[src] > 0)
                    {
                        t[tar] = (long long)t[src] * (long long)f % MOD;
                    }
                    else lease ++;
                }
            }
            while (lease > 0);
            return t;
        }
};

class Solution {
    public:
        const int MOD = 1'000'000'007;
        vector<int> baseUnitConversions(vector<vector<int>>& conversions) {
            
            
            int n = conversions.size() + 1;
            vector<vector<pair<int, int>>> t(n);
            vector<int> res(n);
            for (auto u : conversions)
            {
                t[u[0]].emplace_back(u[1], u[2]);
            }
            dfs(t, res, 0, 1);
            return res;
        }
    private:
        void dfs(vector<vector<pair<int, int>>>& t, vector<int>& res, int st, long long v)
        {
            res[st] = v;
            for (auto& [node, value] : t[st])
            {
                dfs(t, res, node, v * value % MOD);
            }
        }
    };

class Solution {
    public:
        int MOD = 1e9 + 7;
        vector<int> baseUnitConversions(vector<vector<int>>& conversions) {
            vector<int> res(conversions.size() + 1);
            res[0] = 1;
            for (int i = 0; i < conversions.size(); i ++ )
            {
                long long tmp = (long long)res[conversions[i][0]] * conversions[i][2];
                res[conversions[i][1]] = tmp % MOD;
            }
            return res;
        }
    };