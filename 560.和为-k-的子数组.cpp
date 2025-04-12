/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为 K 的子数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> hash;
        hash[0] = 1;
        int sums = 0, cnt = 0;
        for (int i = 0; i < nums.size(); i ++ )
        {
            sums += nums[i];
            if (hash.find(sums - k) != hash.end())
            {
                cnt += hash[sums - k];
            }
            hash[sums] ++;
        }
        return cnt;
    }
};
// @lc code=end

