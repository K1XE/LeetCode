/*
 * @lc app=leetcode.cn id=93 lang=cpp
 *
 * [93] 复原 IP 地址
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> pack;
        vector<string> res;
        if (s.size() < 4 || s.size() > 12) return res;
        this->dfs(0, s, pack, res);
        return res;
    }
    bool check(vector<string>& pack)
    {
        for (auto st : pack)
        {
            int x = stoi(st);
            if (x > 255) return 0;
            if (st.size() > 1 && st[0] == '0') return 0;
        }
        return 1;
    }
    string solve(vector<string>& pack)
    {
        string res;
        for (auto st: pack)
        {
            res += st;
            res += '.';
        }
        res.pop_back();
        return res;
    }
    void dfs(int sta, string& s, vector<string>& pack, vector<string>& res)
    {
        if (pack.size() == 4)
        {
            if (sta == s.size() && check(pack))
            {
                res.emplace_back(solve(pack));
            }
        }
        for (int i = sta; i < min((int)s.size(), sta + 3); i ++ )
        {
            string sub = s.substr(sta, i - sta + 1);
            pack.push_back(sub);
            dfs(i + 1, s, pack, res);
            pack.pop_back();
        }
    }
    
};
// @lc code=end

