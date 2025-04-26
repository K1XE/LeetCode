#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        string findCommonResponse(vector<vector<string>>& responses) {
            map<string, int> res;
            for (int i = 0; i < responses.size(); i ++ )
            {
                map<string, int> hash;
                for (int j = 0; j < responses[i].size(); j ++ )
                {
                    if (hash.find(responses[i][j]) == hash.end())
                    {
                        hash[responses[i][j]] ++;
                    }
                }
                for (auto [key, value] : hash)
                {
                    res[key] ++;
                }
            }
            int maxTimes = 0;
            string maxIdx;
            for (auto [key, value] : res)
            {
                if (value > maxTimes)
                {
                    maxTimes = value;
                    maxIdx = key;
                }
            }
            return maxIdx;
        }
    };