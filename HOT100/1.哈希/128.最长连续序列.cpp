/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 */

// @lc code=start
class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            if (nums.empty()) return 0;
            sort(nums.begin(), nums.end()); 
            int s = 0, e = 1, cnt = 1;
            vector<int> res;
            while(e != nums.size())
            {
                if (nums[e] == nums[e - 1])
                {
                    e ++;
                    continue;
                }
                if (nums[e] - nums[s] == 1)
                {
                    cnt ++;
                }
                else
                {
                    res.push_back(cnt);
                    cnt = 1;
                }
                s = e, e += 1;
            }
            res.push_back(cnt);
            int ans = *max_element(res.begin(), res.end());
            return ans;
        }
    };
// @lc code=end
class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_set<int> nums_set;
            for (auto num : nums)
            {
                nums_set.insert(num);
            }
            int res = 0;
            for (auto num : nums_set)
            {
                if (!nums_set.count(num - 1))
                {
                    int cur_res = 1, cur_num = num;
                    while (nums_set.count(cur_num + 1))
                    {
                        cur_res ++;
                        cur_num ++;
                    }
                    res = max(res, cur_res);
                }
            }
            return res;
        }
    };
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set;
        for (auto num : nums)
        {
            nums_set.insert(num);
        }
        int res = 0;
        for (auto num : nums_set)
        {
            if (!nums_set.count(num - 1))
            {
                int cur_res = 1, cur_num = num;
                while (nums_set.count(cur_num + 1))
                {
                    cur_res ++;
                    cur_num ++;
                }
                res = max(res, cur_res);
            }
        }
        return res;
    }
};