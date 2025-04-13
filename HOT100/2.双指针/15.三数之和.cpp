/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
            vector<vector<int>> res;
            sort(nums.begin(), nums.end());
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                unordered_set<int> get;
                for (int j = i + 1; j < nums.size(); j ++ )
                {
                    int target = - (nums[i] + nums[j]);
                    if (get.count(target))
                    {
                        res.push_back({nums[i], nums[j], target});
                        while (j + 1 < nums.size() && nums[j] == nums[j + 1]) j ++;
                    }
                    get.insert(nums[j]);
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
            vector<vector<int>> res;
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] > 0) break;
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                int l = i + 1, r = nums.size() - 1;
                while (l < r)
                {
                    int sum = nums[i] + nums[l] + nums[r];
                    if (sum == 0)
                    {
                        res.push_back({nums[i], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l + 1]) l ++;
                        while (l < r && nums[r] == nums[r - 1]) r --;
                        l ++, r --;
                    }
                    else if (sum > 0)
                    {
                        r --;
                    }
                    else
                    {
                        l ++;
                    }
                }
            }
            return res;
        }
    };