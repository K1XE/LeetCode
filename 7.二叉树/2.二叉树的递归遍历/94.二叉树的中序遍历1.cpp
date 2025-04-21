/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
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
    vector<int> inorderTraversal(TreeNode* root) {
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
            if (tmp.first->right) stk.emplace(tmp.first->right, 0);
            stk.emplace(tmp.first, 1);
            if (tmp.first->left) stk.emplace(tmp.first->left, 0);
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> inorderTraversal(TreeNode* root) {
            vector<int> res;
            stack<TreeNode*> stk;
            TreeNode* p = root;
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
                    stk.pop();
                    res.push_back(tmp->val);
                    p = tmp->right;
                }
            }
            return res;
        }
    };

class Solution {
    public:
        vector<int> inorderTraversal(TreeNode* root) {
            vector<int> res;
            dfs(root, res);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& res)
        {
            if (! n) return;
            dfs(n->left, res);
            res.push_back(n->val);
            dfs(n->right, res);
        }
    };