/*
 * @lc app=leetcode.cn id=454 lang=cpp
 *
 * [454] 四数相加 II
 */

// @lc code=start
class Solution {
    public:
        int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
            unordered_map<int, int> hash12;
            int res = 0;
            for (int i = 0; i < nums1.size(); i ++ )
            {
                for (int j = 0; j < nums2.size(); j ++ )
                {
                    hash12[nums1[i] + nums2[j]] ++;
                }
            }
            for (int k = 0; k < nums3.size(); k ++ )
            {
                for (int l = 0; l < nums4.size(); l ++ )
                {
                    int target = - (nums3[k] + nums4[l]);
                    if (hash12[target] > 0)
                    {
                        res += hash12[target];
                    }
                }
            }
            return res;
        }
    };
// @lc code=end

