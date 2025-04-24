/*
 * @lc app=leetcode.cn id=783 lang=cpp
 *
 * [783] 二叉搜索树节点最小距离
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
    TreeNode* pre = nullptr;
    long long diff = LLONG_MAX;
    int minDiffInBST(TreeNode* root) {
        dfs(root);
        return diff;
    }
private:
    void dfs(TreeNode* n)
    {
        if (! n) return;
        dfs(n->left);
        if (pre && abs(pre->val - n->val) < diff) diff = abs(pre->val - n->val);
        pre = n;
        dfs(n->right);
    }
};
// @lc code=end

