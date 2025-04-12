/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 */

// @lc code=start
class Solution {
    public:
        bool isHappy(int n) {
            unordered_set<int> hash;
            while (n != 1 && !hash.count(n))
            {
                hash.insert(n);
                n = get_next(n);
            }
            return n == 1;
        }
    private:
        int get_next(int n)
        {
            int res = 0;
            while (n > 0)
            {
                int d = n % 10;
                res += d * d;
                n /= 10;
            }
            return res;
        }
    };
// @lc code=end
class Solution {
    public:
        bool isHappy(int n) {
            string s = to_string(n);
            set<string> hash;
            while (1)
            {
                int sums = 0;
                for (int i = 0; i < s.size(); i ++ )
                {
                    sums += (s[i] - '0') * (s[i] - '0');
                }
                if (sums == 1) return 1;
                sort(s.begin(), s.end());
                if (hash.count(s)) return 0;
                hash.insert(s);
                s = to_string(sums);
            }
            return 0;
        }
    };
