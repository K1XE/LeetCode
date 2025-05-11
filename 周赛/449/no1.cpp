#include "tools.h"
using namespace std;
class Solution {
    public:
        int minDeletion(string s, int k) {
            unordered_map<char, int> hash;
            for (auto ch : s)
            {
                hash[ch] ++;
            }
            if (hash.size() <= k) return 0;
            int res = 0;

            while (hash.size() > k)
            {
                int minV = INT_MAX;
                char minCh;
                for (auto [k, v] : hash)
                {
                    if (v < minV)
                    {
                        minV = v;
                        minCh = k;
                    }
                }
                res += minV;
                hash.erase(minCh);
            }
            return res;
        }
    };