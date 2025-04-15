/*
 * @lc app=leetcode.cn id=71 lang=cpp
 *
 * [71] 简化路径
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk;
        string s;
        istringstream ss(path);
        while (getline(ss, s, '/'))
        {
            if (s.empty() || s == ".") continue;
            else if (s == ".." && stk.size()) stk.pop_back();
            else if (s != "..") stk.push_back(s);
        }
        string res;
        for (auto str : stk)
        {
            res += '/';
            res += str;
        }
        return res.size() ? res : "/";
    }
};
// @lc code=end
class Solution {
    public:
        string simplifyPath(string path) {
            stack<string> stk;
            int i = 0;
            while (i < path.size())
            {
                while (i < path.size() && path[i] == '/') i ++;
                string folder;
                while (i < path.size() && path[i] != '/') folder += path[i ++];
                if (folder == ".") continue;
                else if (folder == ".." && stk.size()) stk.pop();
                else if (folder == ".." && stk.empty()) continue;
                else
                {
                    if (folder.size())
                    {
                        folder += '/';
                        stk.push(folder);
                    }
                }
            }
            stack<string> stk2;
            while (stk.size())
            {
                stk2.push(stk.top());
                stk.pop();
            }
            string res = "/";
            while (stk2.size())
            {
                res += stk2.top();
                if (stk2.size() == 1) res.pop_back();
                stk2.pop();
            }
            return res;
        }
    };
