#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        long long calculateScore(vector<string>& instructions, vector<int>& values) {
            unordered_map<int, bool> hash;
            long long res = 0;
            for (int i = 0; i < instructions.size() && i >= 0;)
            {
                if (hash.find(i) != hash.end() && hash[i] == 1) 
                {
                    return res;
                }
                hash[i] = 1;
                string s = instructions[i];
                if (s == "jump")
                {
                    i = i + values[i];
                }
                if (s == "add")
                {
                    res += values[i];
                    i ++;
                }
            }
            return res;
        }
    };