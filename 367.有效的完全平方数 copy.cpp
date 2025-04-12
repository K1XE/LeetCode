/*
 * @lc app=leetcode.cn id=367 lang=cpp
 *
 * [367] 有效的完全平方数
 */

// @lc code=start
class Solution {
    public:
        bool isPerfectSquare(int num) {
            int l = 0, r = num;
            while (l <= r)
            {
                long long mid = l + ((r - l) >> 1);
                if (mid * mid > num)
                {
                    r = mid - 1;
                }
                else if (mid * mid < num)
                {
                    l = mid + 1;
                }
                else return 1;
            }
            return 0;
        }
    };
// @lc code=end

