/*
 * @lc app=leetcode.cn id=669 lang=cpp
 *
 * [669] 修剪二叉搜索树
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
        TreeNode* trimBST(TreeNode* root, int low, int high) {
            while (root)
            {
                if (root->val >= low && root->val <= high) break;
                if (root->val < low) root = root->right;
                else if (root->val > high) root = root->left;
            }
            TreeNode* cur = root;
            while (cur)
            {
                while (cur->left && cur->left->val < low)
                {
                    cur->left = cur->left->right;
                }
                cur = cur->left;
            }
            cur = root;
            while (cur)
            {
                while(cur->right && cur->right->val > high)
                {
                    cur->right = cur->right->left;
                }
                cur = cur->right;
            }
            return root;
        }
    };
// @lc code=end

class Solution {
    public:
        TreeNode* trimBST(TreeNode* root, int low, int high) {
            TreeNode* node = dfs(root, low, high);
            return node;
        }
    private:
        TreeNode* dfs(TreeNode * n, int low, int high)
        {
            if (! n) return nullptr;
            n->left = dfs(n->left, low, high);
            n->right = dfs(n->right, low, high);
            if (n->val > high || n->val < low) return delete_this_node(n);
            return n;
        }
        TreeNode* delete_this_node(TreeNode* n)
        {
            if (! n) return nullptr;
            TreeNode* res = nullptr;
            if (! n->right) return n->left;
            TreeNode* cur = n->right;
            while (cur->left)
            {
                cur = cur->left;
            }
            cur->left = n->left;
            return n->right;
        }
    };


class Solution {
    public:
        TreeNode* trimBST(TreeNode* root, int low, int high) {
            if (! root) return NULL;
            if (root->val < low) return trimBST(root->right, low, high);
            if (root->val > high) return trimBST(root->left, low, high);
            root->left = trimBST(root->left, low, high);
            root->right = trimBST(root->right, low, high);
            return root;
        }
    };
