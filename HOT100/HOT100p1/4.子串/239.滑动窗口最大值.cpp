/*
 * @lc app=leetcode.cn id=239 lang=cpp
 *
 * [239] 滑动窗口最大值
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        priority_queue<pair<int, int>> heap;
        for (int i = 0; i < k; i ++ )
        {
            heap.emplace(nums[i], i);
        }
        vector<int> res = {heap.top().first};
        for (int i = k; i < nums.size(); i ++ )
        {
            heap.emplace(nums[i], i);
            while (i - heap.top().second + 1 > k)
            {
                heap.pop();
            }
            res.push_back(heap.top().first);
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            vector<int> res;
            deque<int> q;
            for (int i = 0; i < nums.size(); i ++ )
            {
                while (!q.empty() && nums[q.back()] < nums[i])
                {
                    q.pop_back();
                }
                q.push_back(i);
                if (i - q.front() + 1 > k)
                {
                    q.pop_front();
                }
                if (i >= k - 1) res.push_back(nums[q.front()]);
            }
            return res;
        }
    };
