/*
 * @lc app=leetcode.cn id=530 lang=cpp
 *
 * [530] 二叉搜索树的最小绝对差
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
    long long pre = LONG_LONG_MAX;
    long long diff = LONG_LONG_MAX;
    int getMinimumDifference(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                if (pre != LLONG_MAX) diff = min(diff, node->val - pre);
                pre = node->val;
                continue;
            }
            if (node->right) stk.emplace(node->right, 0);
            stk.emplace(node, 1);
            if (node->left) stk.emplace(node->left, 0);
        }
        return diff;
    }
};
// @lc code=end

class Solution {
    public:
        long long pre = LONG_LONG_MAX;
        long long diff = LONG_LONG_MAX;
        int getMinimumDifference(TreeNode* root) {
            if (! root) return diff;
            int a = getMinimumDifference(root->left);
            if (pre != LONG_LONG_MAX) diff = min(diff, root->val - pre);
            pre = root->val;
            int b = getMinimumDifference(root->right);
            return diff;
        }
    };