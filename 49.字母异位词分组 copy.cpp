/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, vector<string>> hash;
            for(string s: strs)
            {
                string sorted_s = s;
                sort(sorted_s.begin(), sorted_s.end());
                hash[sorted_s].push_back(s);
            }
            vector<vector<string>> res;
            
            for(auto [_, value] : hash)
            {
                res.push_back(value);
            }
            return res;
        }
    };        
// @lc code=end

