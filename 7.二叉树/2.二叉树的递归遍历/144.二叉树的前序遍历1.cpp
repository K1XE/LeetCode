/*
 * @lc app=leetcode.cn id=144 lang=cpp
 *
 * [144] 二叉树的前序遍历
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> stk;
        if (root) stk.push(root);
        while (stk.size())
        {
            TreeNode* tmp =  stk.top();
            stk.pop();
            res.push_back(tmp->val);
            if (tmp->right) stk.push(tmp->right);
            if (tmp->left) stk.push(tmp->left);
        }
        return res;
    }
};
// @lc code=end


class Solution {
    public:
        vector<int> preorderTraversal(TreeNode* root) {
            vector<int> res;
            stack<TreeNode*> stk;
            TreeNode* p = root;
            while (stk.size() || p)
            {
                if (p)
                {
                    res.push_back(p->val);
                    stk.push(p);
                    p = p->left;
                }
                else
                {
                    TreeNode* tmp = stk.top();
                    stk.pop();
                    p = tmp->right;
                }
            }
            return res;
        }
    };


class Solution {
    public:
        vector<int> preorderTraversal(TreeNode* root) {
            vector<int> res;
            dfs(root, res);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& res)
        {
            if (! n) return;
            res.push_back(n->val);
            dfs(n->left, res);
            dfs(n->right, res);
        }
    };