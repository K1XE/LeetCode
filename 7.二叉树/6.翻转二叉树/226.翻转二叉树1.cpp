/*
 * @lc app=leetcode.cn id=226 lang=cpp
 *
 * [226] 翻转二叉树
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
    TreeNode* invertTree(TreeNode* root) {
        TreeNode* stk[105];
        int top = -1;
        if (root) stk[++ top] = root;
        while (top >= 0)
        {
            TreeNode* tmp = stk[top --];
            swap(tmp->left, tmp->right);
            if (tmp->right) stk[++ top] = tmp->right;
            if (tmp->left) stk[++ top] = tmp->left;            
        }
        return root;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            dfs(root);
            return root;
        }
    private:
        void dfs(TreeNode* n)
        {
            if (! n) return;
            swap(n->left, n->right);
            dfs(n->left);
            dfs(n->right);
        }
    };