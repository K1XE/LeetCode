/*
 * @lc app=leetcode.cn id=590 lang=cpp
 *
 * [590] N 叉树的后序遍历
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node{
    public:
        int val;
        vector<Node*> children;
        Node(int _val, vector<Node*> _children)
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
    vector<int> postorder(Node* root) {
        vector<int> res;
        if (! root) return {};
        dfs(root, res);
        return res;
    }
private:
    void dfs(Node* n, vector<int>& res)
    {
        if (! n) return;
        for (auto p : n->children)
        {
            dfs(p, res);
        }
        res.push_back(n->val);
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> postorder(Node* root) {
            stack<pair<Node*, bool>> stk;
            vector<int> res;
            if (root) stk.push({root, 0});
            while (stk.size())
            {
                auto tmp = stk.top();
                stk.pop();
                if (tmp.second)
                {
                    res.push_back(tmp.first->val);
                    continue;
                }
                stk.push({tmp.first, 1});
                for (int i = tmp.first->children.size() - 1; i >= 0; i -- )
                {
                    stk.push({tmp.first->children[i], 0});
                }
            }
            return res;
        }
    };
