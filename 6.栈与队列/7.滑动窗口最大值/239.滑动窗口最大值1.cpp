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
        deque<int> q;
        vector<int> res;
        for (int i = 0; i < k; i ++ )
        {
            push(q, nums[i]);
        }
        res.push_back(q.front());
        for (int i = k; i < nums.size(); i ++ )
        {
            pop(q, nums[i - k]);
            push(q, nums[i]);
            res.push_back(q.front());
        }
        return res;
    }
private:
    void push(deque<int>& q, int val)
    {
        while (q.size() && val > q.back()) q.pop_back();
        q.push_back(val);
    }
    void pop(deque<int>& q, int val)
    {
        if (q.size() && q.front() == val) q.pop_front();
    }
};
// @lc code=end

