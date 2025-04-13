/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 */

// @lc code=start
class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_set<int> hash(nums.begin(), nums.end());
            int maxNum = 0;
            for (auto x : hash)
            {
                if (!hash.count(x - 1))
                {
                    int cur_num = 1, cur_x = x;
                    while (hash.count(++ cur_x))
                    {
                        cur_num ++;
                    }
                    maxNum = max(cur_num, maxNum);
                }
            }
            return maxNum;
        }
    };
// @lc code=end
