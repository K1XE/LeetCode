/*
 * @lc app=leetcode.cn id=701 lang=cpp
 *
 * [701] 二叉搜索树中的插入操作
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct TreeNode
{
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
        if (! root)
        {
            TreeNode* node = new TreeNode(val);
            return node;
        }
        TreeNode* parent = root;
        TreeNode* cur = root;
        while (cur)
        {
            parent = cur;
            if (cur->val > val) cur = cur->left;
            else if (cur->val < val) cur = cur->right;
        }
        TreeNode* node = new TreeNode(val);
        if (node->val > parent->val) parent->right = node;
        else parent->left = node;
        return root;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* insertIntoBST(TreeNode* root, int val) {
            TreeNode* node = dfs(root, val);
            return root ? root : node;
        }
    private:
        TreeNode* dfs(TreeNode* n, int val)
        {
            if (! n)
            {
                TreeNode* node = new TreeNode(val);
                return node;
            }
            if (n->val > val)
            {
                n->left = dfs(n->left, val);
            }
            if (n->val < val)
            {
                n->right = dfs(n->right, val);
            }
            return n;
        }
    };