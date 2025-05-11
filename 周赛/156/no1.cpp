#include "tools.h"
using namespace std;
class Solution {
    public:
        int maxFreqSum(string s) {
            unordered_map<char, int> hash1, hash2;
            for (int i = 0; i < s.size(); i ++ )
            {
                if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') hash1[s[i]] ++;
                else hash2[s[i]] ++;
            }
            int max1 = 0, max2 = 0;
            for (auto [k, v] : hash1)
            {
                if (v > max1) max1 = v;
            }
            for (auto [k, v] : hash2)
            {
                if (v > max2) max2 = v;
            }
            return max1 + max2;
        }

    };

