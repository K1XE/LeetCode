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
                int tmp = target - nums[i];
                auto it = hash.find(tmp);
                if (it != hash.end())
                {
                    return {i, it->second};
                }
                hash[nums[i]] = i;
            }
            return {};
        }
    };
// @lc code=end
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> hash;
            for (int i = 0; i < nums.size(); i ++ )
            {
                int tmp = target - nums[i];
                auto it = hash.find(tmp);
                if (it != hash.end())
                {
                    return {i, it->second};
                }
                hash[nums[i]] = i;
            }
            return {};
        }
    };