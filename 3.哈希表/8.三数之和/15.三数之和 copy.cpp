/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
            sort(nums.begin(), nums.end());
            vector<vector<int>> res;
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] > 0) break;
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                unordered_set<int> set;
                for (int k = i + 1; k < nums.size(); k ++ )
                {
                    if (k > i + 2 && nums[k] == nums[k - 1] && nums[k - 1] == nums[k - 2]) continue;
                    int target = - (nums[i] + nums[k]);
                    if (set.find(target) != set.end())
                    {
                        res.push_back({nums[i], target, nums[k]});
                        set.erase(target);
                    }
                    else
                    {
                        set.insert(nums[k]);
                    }
                }
            }
            return res;
        }
    };
// @lc code=end

class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
            sort(nums.begin(), nums.end());
            int i = 0;
            vector<vector<int>> res;
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] >0) break;
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                int target = - nums[i];
                int l = i + 1, r = nums.size() - 1;
    
                while (l < r)
                {
                    if (target == nums[l] + nums[r])
                    {
                        res.push_back({nums[i], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l + 1]) l ++;
                        while (l < r && nums[r] == nums[r - 1]) r --;
                        l ++, r --;
                    }
                    else if (target > nums[l] + nums[r])
                    {
                        l ++;
                    }
                    else
                    {
                        r --;
                    }
    
                }
            }
            return res;
        }
    };