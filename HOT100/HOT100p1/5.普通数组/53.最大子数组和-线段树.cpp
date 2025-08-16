/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        return get(nums, 0, nums.size() - 1).msum;
    }
private:
    struct state {
        int lsum, rsum, msum, isum;
    };
    state pushUp(state l, state r)
    {
        int isum = l.isum + r.isum;
        int lsum = max(l.lsum, l.isum + r.lsum);
        int rsum = max(r.rsum, r.isum + l.rsum);
        int msum = max({l.msum, r.msum, l.rsum + r.lsum});
        return {lsum, rsum, msum, isum};
    }
    state get(vector<int>& a, int l, int r)
    {
        if (l == r)
        {
            return {a[l], a[l], a[l], a[l]};
        }
        int m = (l + r) >> 1;
        state lSub = get(a, l, m);
        state rSub = get(a, m + 1, r);
        return pushUp(lSub, rSub);
    }
};
// @lc code=end
