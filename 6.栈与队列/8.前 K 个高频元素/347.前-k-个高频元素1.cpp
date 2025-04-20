/*
 * @lc app=leetcode.cn id=347 lang=cpp
 *
 * [347] 前 K 个高频元素
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        auto cmp = [](pair<int, int> a, pair<int, int> b)
        {
            return a.first > b.first;
        };
        unordered_map<int, int> hash;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> heap(cmp);
        vector<int> res;
        for (auto x : nums)
        {
            hash[x] ++;
        }
        for (auto [key, v] : hash)
        {
            heap.emplace(v, key);
            if (heap.size() > k) heap.pop();
        }
        while (heap.size()) res.push_back(heap.top().second), heap.pop();
        return res;
    }
};
// @lc code=end

