/*
 * @lc app=leetcode.cn id=350 lang=cpp
 *
 * [350] 两个数组的交集 II
 */

// @lc code=start
class Solution {
    public:
        vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
            unordered_map<int, int> hash;
            vector<int> res;
            for (auto x : nums1)
            {
                hash[x] ++;
            }
            for (auto x :nums2)
            {
                if (hash[x] -- > 0) res.push_back(x);
            }
            return res;
        }
    };
// @lc code=end

class Solution {
    public:
        vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
            array<int, 1005> hash1{}, hash2{};
            vector<int> res;
            for (int i = 0; i < nums1.size(); i ++ )
            {
                hash1[nums1[i]] ++; 
            }
            for (int i = 0; i < nums2.size(); i ++ )
            {
                hash2[nums2[i]] ++;
            }
            for (int i = 0; i < 1005; i ++ )
            {
                if (hash1[i] > 0 && hash2[i] > 0)
                {
                    int minVal = min(hash1[i], hash2[i]);
                    while (minVal --)
                    {
                        res.push_back(i);
                    }
                }
            }
            return res;
        }
    };