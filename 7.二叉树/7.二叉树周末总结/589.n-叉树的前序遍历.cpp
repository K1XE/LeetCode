/*
 * @lc app=leetcode.cn id=589 lang=cpp
 *
 * [589] N 叉树的前序遍历
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
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
    vector<int> preorder(Node* root) {
        vector<int> res;
        dfs(root, res);
        return res;
    }
private:
    void dfs(Node* n, vector<int>& res)
    {
        if (! n) return;
        res.push_back(n->val);
        for (auto p : n->children)
        {
            dfs(p, res);
        }
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> preorder(Node* root) {
            vector<int> res;
            stack<pair<Node*, bool>> stk;
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
                for (int i = tmp.first->children.size() - 1; i >= 0; i -- )
                {
                    stk.push({tmp.first->children[i], 0});
                }
                stk.push({tmp.first, 1});
            }
            return res;
        }
    };