/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 */

// @lc code=start
class Solution {
    public:
        int totalFruit(vector<int>& fruits) {
            unordered_map<int, int> hash;
            int i = 0, j = 0;
            int maxLen = INT32_MIN, len = INT32_MIN;
            for (; j < fruits.size(); j ++ )
            {
                hash[fruits[j]] ++;
                while (hash.size() > 2)
                {
                    hash[fruits[i]] --;
                    if (hash[fruits[i]] == 0) hash.erase(fruits[i]);
                    i ++;
                }
                len = j - i + 1;
                maxLen = max(maxLen, len);
            }
            return maxLen == INT32_MIN ? fruits.size() : maxLen; 
        }
    };
// @lc code=end
