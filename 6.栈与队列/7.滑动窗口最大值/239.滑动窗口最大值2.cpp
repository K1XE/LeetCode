/*
 * @lc app=leetcode.cn id=239 lang=cpp
 *
 * [239] 滑动窗口最大值
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    deque<int> q;
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        for (int i = 0; i < k; i ++ )
        {
            push(nums[i]);
        }
        res.push_back(q.front());
        for (int i = k; i < nums.size(); i ++ )
        {
            pop(nums[i - k]);
            push(nums[i]);
            res.push_back(q.front());
        }
        return res;
    }
private:
    void push(int x)
    {
        while (q.size() && q.back() < x) q.pop_back();
        q.push_back(x);
    }
    void pop(int x)
    {
        if (q.front() == x) q.pop_front();
    }
};
// @lc code=end


class Solution {
    public:
        vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            deque<int> q;
            vector<int> res;
            for (int i = 0; i < nums.size(); i ++ )
            {
                while (q.size() && nums[i] > nums[q.back()]) q.pop_back();
                q.push_back(i);
                if (i - q.front() + 1 > k) q.pop_front();
                if (i + 1 >= k) res.push_back(nums[q.front()]);
            }
            return res;
        }
    };

class Solution {
    public:
        vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            priority_queue<pair<int, int>> heap;
            vector<int> res;
            for (int i = 0; i < k; i ++ )
            {
                heap.emplace(nums[i], i);
            }
            res.push_back(heap.top().first);
            for (int i = k; i < nums.size(); i ++ )
            {
                heap.emplace(nums[i], i);
                while (i - heap.top().second + 1 > k) heap.pop();
                res.push_back(heap.top().first);
            }
            return res;
        }
    };