/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int res = 0;
        int pre = -1, suf = -1;
        int l = 0, r = n - 1;
        while (l <= r)
        {
            pre = max(pre, height[l]);
            suf = max(suf, height[r]);
            if (pre > suf)
            {
                res += suf - height[r];
                r --;
            }
            else
            {
                res += pre - height[l];
                l ++;
            }
        }
        return res;
    }
};
// @lc code=end


class Solution {
    public:
        int trap(vector<int>& height) {
            int n = height.size();
            int res = 0;
            vector<int> suf(n);
            suf[n - 1] = height[n - 1];
            for (int i = n - 2; i >= 0; i -- )
            {
                suf[i] = max(height[i], suf[i + 1]);
            }
            int pre = height[0];
            for (int i = 1; i < n; i ++ )
            {
                pre = max(height[i], pre);
                if (min(suf[i], pre) - height[i] > 0) res += min(suf[i], pre) - height[i];
            }
            return res;
        }
    };

class Solution {
    public:
        int trap(vector<int>& height) {
            int n = height.size();
            int res = 0;
            vector<int> pre(n), suf(n);
            pre[0] = height[0], suf[n - 1] = height[n - 1];
            for (int i = 1; i < n; i ++ )
            {
                pre[i] = max(height[i], pre[i - 1]);
            }
            for (int i = n - 2; i >= 0; i -- )
            {
                suf[i] = max(height[i], suf[i + 1]);
            }
            for (int i = 0; i < n; i ++ )
            {
                if (min(suf[i], pre[i]) - height[i] > 0) res += min(suf[i], pre[i]) - height[i];
            }
            return res;
        }
    };