/*
 * @lc app=leetcode.cn id=347 lang=cpp
 *
 * [347] 前 K 个高频元素
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        auto cmp = [](const pair<int, int>& a, const pair<int, int>& b)
        {
            return a.first > b.first;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>,decltype(cmp)> heap(cmp);
        unordered_map<int, int> hash;
        vector<int> res;
        for (auto x : nums)
        {
            hash[x] ++;
        }
        for(auto [key, val] : hash)
        {
            heap.emplace(val, key);
            if (heap.size() > k)
            {
                heap.pop();
            }
        }
        while (heap.size())
        {
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            priority_queue<pair<int, int>> heap;
            unordered_map<int, int> hash;
            vector<int> res;
            for (int i = 0; i < nums.size(); i ++ )
            {
                hash[nums[i]] ++;
            }
            for (auto [key, val] : hash)
            {
                heap.emplace(val, key);
            }
            while (k --)
            {
                res.push_back(heap.top().second);
                heap.pop();
            }
            return res;
        }
    };
