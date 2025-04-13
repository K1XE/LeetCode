/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public:
        int trap(vector<int>& height) {
            int l = 0, r = height.size() - 1;
            int pre_max = -1, suf_max = -1;
            int res = 0;
            while (l <= r)
            {
                pre_max = max(pre_max, height[l]);
                suf_max = max(suf_max, height[r]);
                res += pre_max > suf_max ? suf_max - height[r --] : pre_max - height[l ++];
            }
            return res;
        }
    };
// @lc code=end

class Solution {
    public:
        int trap(vector<int>& height) {
            vector<int> pre_max, suf_max;
            int cur_pre_max = -1;
            for (auto h : height)
            {
                cur_pre_max = max(cur_pre_max, h);
                pre_max.push_back(cur_pre_max);
            }
            int cur_suf_max = -1;
            for (int i = height.size() - 1; i >= 0; i -- )
            {
                cur_suf_max = max(cur_suf_max, height[i]);
                suf_max.push_back(cur_suf_max);
            }
            reverse(suf_max.begin(), suf_max.end());
            int res = 0;
            for (int i = 0; i < height.size(); i ++ )
            {
                res += min(pre_max[i], suf_max[i]) - height[i];
            }
            return res;
        }
    };