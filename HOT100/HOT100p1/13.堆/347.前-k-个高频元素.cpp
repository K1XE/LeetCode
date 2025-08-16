/*
 * @lc app=leetcode.cn id=347 lang=cpp
 *
 * [347] 前 K 个高频元素
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hash;
        int max_cnt = 0;
        for (auto x : nums)
        {
            hash[x] ++;
            max_cnt = max(max_cnt, hash[x]);
        }
        vector<vector<int>> bucket(max_cnt + 1);
        for (auto& [key, val] : hash)
        {
            bucket[val].push_back(key);
        }
        vector<int> res;
        for (int i = max_cnt; i >= 0; i -- )
        {
            res.insert(res.end(), bucket[i].begin(), bucket[i].end());
            k -= bucket[i].size();
            if (k <= 0) break;
        }
        return res;

    }
};
// @lc code=end

