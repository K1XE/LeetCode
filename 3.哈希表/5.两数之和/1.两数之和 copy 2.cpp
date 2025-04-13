/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> hash;
            for (int i = 0; i < nums.size(); i ++ )
            {
                
            }
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (hash.find(target - nums[i]) != hash.end())
                {
                    return {i, hash[target - nums[i]]};
                }
                hash[nums[i]] = i;
            }
            return {-1, -1};
        }
    };
// @lc code=end
