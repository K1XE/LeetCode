/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根 
 */

// @lc code=start
class Solution {
    public:
        int mySqrt(int x) {
            int l = 0, r = x - 1;
            if (x == 0) return 0;
            if (x == 1) return 1;
            while (l <= r)
            {
                long long mid = l + ((r - l) >> 1);
                if (mid * mid > x)
                {
                    r = mid - 1;
                }
                else if (mid * mid < x)
                {
                    l = mid + 1;
                }
                else return mid;
            }
            return r;
        }
    };
// @lc code=end
