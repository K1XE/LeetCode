/*
 * @lc app=leetcode.cn id=700 lang=cpp
 *
 * [700] 二叉搜索树中的搜索
 */
#include <bits/stdc++.h>
#include <ranges>
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
    TreeNode* searchBST(TreeNode* root, int val) {
        stack<TreeNode*> stk;
        if (root) stk.emplace(root);
        while (stk.size())
        {
            TreeNode* tmp = stk.top();
            stk.pop();
            if (tmp->val == val) return tmp;
            if (tmp->val < val && tmp->right) stk.emplace(tmp->right);
            if (tmp->val > val && tmp->left) stk.emplace(tmp->left);
        }
        return NULL;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* searchBST(TreeNode* root, int val) {
            if (! root) return NULL;
            if (root->val == val) return root;
            else if (root->val > val)
            {
                return searchBST(root->left, val);
            }
            else return searchBST(root->right, val);
            return root;
        }
    };