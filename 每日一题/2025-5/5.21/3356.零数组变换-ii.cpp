/*
 * @lc app=leetcode.cn id=3356 lang=cpp
 *
 * [3356] 零数组变换 II
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> cover(n);
        int k = 0, sums_d = 0;
        for (int i = 0; i < n; i ++ )
        {
            sums_d += cover[i];
            int x = nums[i];
            while (k < queries.size() && x + sums_d > 0)
            {
                int l = queries[k][0], r = queries[k][1], times = queries[k][2];
                cover[l] -= times;
                if (r + 1 < n) cover[r + 1] += times;
                if (l <= i && i <= r) sums_d -= times;
                k ++;
            }
            if (x + sums_d > 0) return -1;
        }
        return k;
    }
};
// @lc code=end

class Solution {
    public:
        int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
            int n = nums.size();
            auto check = [&](int u) -> bool
            {
                vector<int> cover(n, 0);
                for (int i = 0; i < u; i ++ )
                {
                    vector<int> tmp = queries[i];
                    int l = tmp[0], r = tmp[1], times = tmp[2];
                    cover[l] -= times;
                    if (r + 1 < n) cover[r + 1] += times;
                }
                int sums_d = 0;
                for (int i = 0; i < n; i ++ )
                {
                    sums_d += cover[i];
                    if (nums[i] + sums_d > 0) return 0;
                }
                return 1;
            };
            int res = -1;
            int l = 0, r = queries.size();
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (check(mid)) res = mid, r = mid - 1;
                else l = mid + 1;
            }
            return res;
        }
    };