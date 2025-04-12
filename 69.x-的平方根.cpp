/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根 
 */

// @lc code=start
class Solution {
    public:
        int mySqrt(int x) {
            long long l = 0, r = x;
            while (l <= r)
            {
                long long mid = l + r >> 1;
                long long diff = x - mid * mid;
                if (diff > 0)
                {
                    l = mid + 1;
                }
                else if (diff < 0)
                {
                    r = mid - 1;
                }
                else
                {
                    return mid;
                }
            }
            return r;
        }
    };
// @lc code=end
class Solution {
    public:
        int mySqrt(int x) {
            if (x == 0) return 0;
            double a = x, x0 = x;
            while (1)
            {
                double x1 = (x0 + a / x0) / 2;
                if (fabs(x0 - x1) < 1e-7) break;
                x0 = x1;
            }
            return int(x0);
        }
    };
