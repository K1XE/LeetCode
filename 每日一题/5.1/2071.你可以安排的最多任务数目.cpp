/*
 * @lc app=leetcode.cn id=2071 lang=cpp
 *
 * [2071] 你可以安排的最多任务数目
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        ranges::sort(tasks);
        ranges::sort(workers);
        int l = 1, r = min(tasks.size(), workers.size()), res = 0;
        while (l <= r)
        {
            int mid = l + r >> 1;
            if (check(tasks, workers, pills, strength, mid))
            {
                res = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        return res;
    }
private:
    bool check(vector<int>& t, vector<int>& w, int p, int s, int m)
    {
        multiset<int> ws;
        for (int i = w.size() - m; i < w.size(); i ++ )
        {
            ws.insert(w[i]);
        }
        for (int i = m - 1; i >= 0; i -- )
        {
            if (auto it = prev(ws.end()); *it >= t[i])
            {
                ws.erase(it);
            }
            else
            {
                if (! p) return 0;
                auto rep = ws.lower_bound(t[i] - s);
                if (rep == ws.end()) return 0;
                p --;
                ws.erase(rep);
            }
        }
        return 1;
    }
};
// @lc code=end

