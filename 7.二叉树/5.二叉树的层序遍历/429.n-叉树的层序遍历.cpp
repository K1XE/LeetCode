/*
 * @lc app=leetcode.cn id=429 lang=cpp
 *
 * [429] N 叉树的层序遍历
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
    public:
        int val;
        vector<Node*> children;
        Node(int _val, vector<Node*>& _children)
        {
            val = _val;
            children = _children;
        }
};

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        dfs(root, res, 0);
        return res;
    }
private:
    void dfs(Node* n, vector<vector<int>>& res, int depth)
    {
        if (!n) return;
        if (res.size() == depth) res.emplace_back();
        res[depth].push_back(n->val);
        for (auto p : n->children)
        {
            dfs(p, res, depth + 1);
        }
    }
};
// @lc code=end
class Solution {
    public:
        vector<vector<int>> levelOrder(Node* root) {
            queue<Node*> q;
            vector<vector<int>> res;
            if (root) q.push(root);
            while (q.size())
            {
                vector<int> level;
                int n = q.size();
                while (n --)
                {
                    Node* tmp = q.front();
                    q.pop();
                    level.push_back(tmp->val);
                    for (auto p : tmp->children)
                    {
                        q.push(p);
                    }
                }
                res.emplace_back(level);
            }
            return res;
        }
    };
