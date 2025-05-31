/*
 * @lc app=leetcode.cn id=1007 lang=cpp
 *
 * [1007] 行相等的最少多米诺旋转
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int minDominoRotations(vector<int>& ts, vector<int>& bs) {
        int res = min(solve(ts, bs, ts[0]), solve(ts, bs, bs[0]));
        return res == INT_MAX ? -1 : res;
    }
private:
    int solve(vector<int>& ts, vector<int>& bs, int tar)
    {
        int top = 0, bot = 0;
        for (int i = 0; i < ts.size(); i ++ )
        {
            int x = ts[i], y = bs[i];
            if (x != tar && y != tar) return INT_MAX;
            if (x != tar) top ++;
            else if (y != tar) bot ++;
        }
        return min(top, bot);
    }
};
// @lc code=end

class Solution {
    public:
        int minDominoRotations(vector<int>& ts, vector<int>& bs) {
            unordered_map<int, int> hash;
            for (int i = 0; i < ts.size(); i ++ )
            {
                if (ts[i] != bs[i])
                {
                    hash[ts[i]] ++;
                    hash[bs[i]] ++;
                }
                else hash[ts[i]] ++;
            }
            int maxK = -1, maxV = -1;
            for (auto [key, val] : hash)
            {
                if (val > maxV)
                {
                    maxV = val;
                    maxK = key;
                }
            }
            if (maxV < ts.size()) return -1;
            int cnt1 = 0, cnt2 = 0;
            for (auto x : ts)
            {
                if (x == maxK) continue;
                else cnt1 ++;
            }
            for (auto x : bs)
            {
                if (x == maxK) continue;
                else cnt2 ++;
            }
            return min(cnt1, cnt2);
        }
    };