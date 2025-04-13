/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            sort(nums.begin(), nums.end());
            int bg = -1, cnt = 0;
            bool flag = 1;
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] == val)
                {
                    if (flag) bg = i, flag = 0;
                    cnt ++;
                }
            }
            for (int i = 0; i < cnt; i ++ )
            {
                int tmp = nums[nums.size() - 1 - i];
                nums[nums.size() - 1 - i] = nums[bg + i];
                nums[bg + i] = tmp;
            }
            return nums.size() - cnt;
        }
    };
// @lc code=end
class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int left = 0, right = nums.size() - 1;
            while (left <= right)
            {
                if (nums[left] != val) left ++;
                else 
                {
                    nums[left] = nums[right --];
                }
            }
            return left;
        }
    };
