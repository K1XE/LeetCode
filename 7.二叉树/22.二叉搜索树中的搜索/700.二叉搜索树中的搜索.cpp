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
        TreeNode* p = root;
        while (p)
        {
            if (p->val == val) return p;
            else if (p->val > val) p = p->left;
            else p = p->right;
        }
        return nullptr;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* searchBST(TreeNode* root, int val) {
            return dfs(root, val);
        }
    private:
        TreeNode* dfs(TreeNode* n, int val)
        {
            if (! n) return nullptr;
            if (n->val == val) return n;
            if (n->val > val) return dfs(n->left, val);
            if (n->val < val) return dfs(n->right, val);
            return nullptr;
        }
    };