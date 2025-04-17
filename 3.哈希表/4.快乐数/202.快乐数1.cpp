/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool isHappy(int n) {
        int fast = n, slow = n;
        do
        {
            slow = getNum(slow);
            fast = getNum(fast);
            fast = getNum(fast);
        } while (fast != slow);
        return fast == 1;
    }
    int getNum(int n)
    {
        int sums = 0;
        while (n > 0)
        {
            int x = n % 10;
            sums += x * x;
            n /= 10;
        }
        return sums;
    }
};
// @lc code=end
class Solution {
    public:
        bool isHappy(int n) {
            set<int> seen;
            while (n != 1 && seen.count(n) == 0)
            {
                seen.insert(n);
                n = getNums(n);
            }
            return n == 1;
        }
    private:
        int getNums(int n)
        {
            int sums = 0;
            while (n)
            {
                int x = n % 10;
                sums += x * x;
                n /= 10;
            }
            return sums;
        }
    };
