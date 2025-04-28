/*
 * @lc app=leetcode.cn id=701 lang=cpp
 *
 * [701] 二叉搜索树中的插入操作
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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        stack<TreeNode*> stk;
        if (root) stk.emplace(root);
        TreeNode* pre = NULL;
        while (stk.size())
        {
            TreeNode* tmp = stk.top();
            pre = tmp;
            stk.pop();
            if (pre->val > val && pre->left) stk.emplace(pre->left);
            else if (pre->val < val && pre->right) stk.emplace(pre->right);
        }
        TreeNode* tmp = new TreeNode(val);
        if (! pre) return tmp;
        pre->val > val ? pre->left = tmp : pre->right = tmp;
        return root;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* insertIntoBST(TreeNode* root, int val) {
            if (! root)
            {
                TreeNode* tmp = new TreeNode(val);
                return tmp;
            }
            if (root->val > val)
            {
                root->left = insertIntoBST(root->left, val);
            }
            if (root->val < val)
            {
                root->right = insertIntoBST(root->right, val);
            }
            return root;
        }
    };