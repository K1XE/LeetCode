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
            int cnt = 0, i = 0, len = 0;
            for (int j = 0; j < fruits.size(); j ++ )
            {
                hash[fruits[j]] += 1;
                while (hash.size() > 2)
                {
                    auto it = hash.find(fruits[i]);
                    --it->second;
                    if (it->second == 0)
                    {
                        hash.erase(it);
                    }
                    i ++;
                }
                len = j - i + 1;
                cnt = cnt > len ? cnt : len;
            }
            return cnt;
        }
    };
// @lc code=end
class Solution {
    public:
        int totalFruit(vector<int>& fruits) {
            unordered_map<int, int> hash;
            int cnt = 0, i = 0, len = 0;
            for (int j = 0; j < fruits.size(); j ++ )
            {
                hash[fruits[j]] += 1;
                if (hash.size() > 2)
                {
                    int tmp = j - i;
                    cnt = cnt > tmp ? cnt : tmp;
                }
                while (hash.size() > 2)
                {
                    hash[fruits[i]] -= 1;
                    if (hash[fruits[i]] == 0)
                    {
                        hash.erase(fruits[i]);
                    }
                    i ++;
                }
                len = j - i + 1;
                cnt = cnt > len ? cnt : len;
            }
            return cnt;
        }
    };
class Solution {
    public:
        int totalFruit(vector<int>& fruits) {
            unordered_map<int, int> hash;
            int cnt = 0, i = 0, len = 0;
            for (int j = 0; j < fruits.size(); j ++ )
            {
                hash[fruits[j]] += 1;
                if (hash.size() > 2)
                {
                    int tmp = j - i + 1 - 1;
                    cnt = cnt > tmp ? cnt : tmp;
                }
                while (hash.size() > 2)
                {
                    hash[fruits[i]] -= 1;
                    if (hash[fruits[i]] == 0)
                    {
                        hash.erase(fruits[i]);
                    }
                    i ++;
                }
                len = j - i + 1;
                cnt = cnt > len ? cnt : len;
            }
            return cnt;
        }
    };