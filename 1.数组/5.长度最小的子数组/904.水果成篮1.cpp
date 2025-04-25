/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int i = 0;
        int maxLen = 0;
        unordered_map<int, int> hash;
        for (int j = 0; j < fruits.size(); j ++ )
        {
            hash[fruits[j]] ++;
            if (hash.size() > 2) maxLen = max(j - i, maxLen);
            while (hash.size() > 2)
            {
                if (-- hash[fruits[i]] == 0) hash.erase(fruits[i]);
                i ++;
            }
            maxLen = max(j - i + 1, maxLen);
        }
        return maxLen;
    }
};
// @lc code=end

