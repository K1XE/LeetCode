/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
 */

// @lc code=start
class Solution {
    public:
        vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
            array<int, 1005> hash1;
            array<bool, 1005> flag;
            vector<int> res;
            for (int i = 0; i < nums1.size(); i ++ )
            {
                hash1[nums1[i]] ++;
            }
            for (int i = 0; i < nums2.size(); i ++ )
            {
                if (hash1[nums2[i]] > 0 && !flag[nums2[i]])
                {
                    res.push_back(nums2[i]);
                    flag[nums2[i]] = 1;
                }
            }
            return res;
        }
    };
// @lc code=end

