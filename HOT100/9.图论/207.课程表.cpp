/*
 * @lc app=leetcode.cn id=207 lang=cpp
 *
 * [207] 课程表
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> g(numCourses);
        vector<int> ind(numCourses);
        for (auto& p : prerequisites)
        {
            int u = p[0], v = p[1];
            g[v].push_back(u);
            ind[u] ++;
        }
        int cnt = 0;
        queue<int> q;
        for (int i = 0; i < numCourses; i ++ )
        {
            if (ind[i] == 0) q.push(i);
        }
        while (q.size())
        {
            int u = q.front(); q.pop();
            cnt ++;
            for (auto& v : g[u])
            {
                if (-- ind[v] == 0) q.push(v);
            }
        }
        return cnt == numCourses;
    }
};
// @lc code=end

class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {

        vector<unordered_set<int>> g(numCourses);
        for (auto &p : prerequisites)
        {
            int u = p[0], v = p[1];
            g[u].insert(v);
        }
        int ok = 0;
        int prevok = -1;
        vector<bool> rm(numCourses, 0);
        while (ok < numCourses)
        {
            if (prevok == ok)
                break;
            prevok = ok;
            for (int i = 0; i < numCourses; i++)
            {
                if (g[i].empty() && !rm[i])
                {
                    ok++;
                    rm[i] = 1;
                    for (int j = 0; j < numCourses; j++)
                    {
                        if (g[j].count(i))
                            g[j].erase(i);
                    }
                }
            }
        }
        return ok == numCourses;
    }
};