#include "tools.h"
class Solution {
    public:
        static bool cmp(pair<int, int> a, pair<int, int> b)
        {
            return a.second < b.second;
        }
        int maxSubstrings(string word) {
            unordered_map<char, vector<int>> seek;
            int n = word.size();
            for (int i = 0; i < n; i ++ )
            {
                seek[word[i]].push_back(i);
            }
            vector<pair<int,int>> pack;
            for (auto& [k, v] : seek)
            {
                for (auto i : v)
                {
                    auto it = lower_bound(v.begin(), v.end(), i + 3);
                    if (it != v.end())
                    {
                        pack.emplace_back(i, *it);
                    }
                }
            }
            ranges::sort(pack, cmp);
            
            int lastr = -1;
            int res = 0;
            for (auto [l, r] : pack)
            {
                if (lastr == -1)
                {
                    res += 1;
                    lastr = r;
                }
                else
                {
                    if (l > lastr)
                    {
                        res += 1;
                        lastr = r;
                    }
                }
            }
            return res;
        }
    };