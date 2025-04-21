/*
 * @lc app=leetcode.cn id=145 lang=cpp
 *
 * [145] 二叉树的后序遍历
 */
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto tmp = stk.top();
            stk.pop();
            if (tmp.second)
            {
                res.push_back(tmp.first->val);
                continue;
            }
            stk.emplace(tmp.first, 1);
            if (tmp.first->right) stk.emplace(tmp.first->right, 0);
            if (tmp.first->left) stk.emplace(tmp.first->left, 0);
        }
        return res;
    }
};
// @lc code=end


class Solution {
    public:
        vector<int> postorderTraversal(TreeNode* root) {
            vector<int> res;
            stack<TreeNode*> stk;
            TreeNode* p = root;
            TreeNode* pre = new TreeNode(0);
            while (stk.size() || p)
            {
                if (p)
                {
                    stk.push(p);
                    p = p->left;
                }
                else
                {
                    TreeNode* tmp = stk.top();
                    if (tmp->right && pre != tmp->right)
                    {
                        p = tmp->right;
                    }
                    else
                    {
                        stk.pop();
                        res.push_back(tmp->val);
                        pre = tmp;
                    }
                }
            }
            return res;
        }
    };

class Solution {
    public:
        vector<int> postorderTraversal(TreeNode* root) {
            vector<int> res;
            dfs(root, res);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& res)
        {
            if (! n) return;
            dfs(n->left, res);
            dfs(n->right, res);
            res.push_back(n->val);
        }
    };