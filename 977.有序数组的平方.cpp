/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */

// @lc code=start
class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            vector<int> backup(nums.size(), 0);
            int s1 = 0, s2 = nums.size() - 1, s3 = backup.size() - 1;
            for (int i = s1, j = s2; i <= j; )
            {
                int a = nums[i] * nums[i], b = nums[j] * nums[j];
                if (a < b)
                {
                    backup[s3 -- ] = b;
                    j --;
                }
                else
                {
                    backup[s3 -- ] = a;
                    i ++;
                }
            }
    
            return backup;
        }
    };
// @lc code=end
class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            int idx = nums.size();
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] >= 0)
                {
                    idx = i;
                    break;
                }
            }
            for (int i = 0; i < idx; i ++ )
            {
                nums[i] = abs(nums[i]);
            }
            int l = 0, r = idx - 1;
            while (l < r)
            {
                swap(nums[l ++ ], nums[r -- ]);
            }
            vector<int> backup(nums.size(), 0);
            int s1 = 0, s2 = idx, s3 = 0;
            while (s1 < idx && s2 < nums.size())
            {
                if (nums[s1] > nums[s2]) backup[s3 ++ ] = nums[s2 ++ ];
                else backup[s3 ++ ] = nums[s1 ++ ];
            }
            while (s1 < idx) backup[s3 ++ ] = nums[s1 ++ ];
            while (s2 < nums.size()) backup[s3 ++ ] = nums[s2 ++ ];
            for (int i = 0; i < backup.size(); i ++ )
            {
                backup[i] *= backup[i];
            }
    
            return backup;
        }
    };
class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            int idx = nums.size();
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] >= 0)
                {
                    idx = i;
                    break;
                }
            }
            // cout << idx << endl;
            for (int i = 0; i < idx; i ++ )
            {
                nums[i] = abs(nums[i]);
            }
            int l = 0, r = idx - 1;
            while (l < r)
            {
                swap(nums[l ++ ], nums[r -- ]);
            }
            // for (auto x : nums)
            // {
            //     cout << x << " ";
            // }
            // cout << endl;
            vector<int> backup;
            int s1 = 0, s2 = idx, s3 = 0;
            while (s1 < idx && s2 < nums.size())
            {
                if (nums[s1] > nums[s2]) backup.push_back(nums[s2 ++ ]);
                else backup.push_back(nums[s1 ++ ]);
            }
            while (s1 < idx) backup.push_back(nums[s1 ++ ]);
            while (s2 < nums.size()) backup.push_back(nums[s2 ++ ]);
            // for (auto x : backup)
            // {
            //     cout << x << " ";
            // }
            // cout << endl;
            for (int i = 0; i < backup.size(); i ++ )
            {
                backup[i] *= backup[i];
            }
    
            return backup;
        }
    };