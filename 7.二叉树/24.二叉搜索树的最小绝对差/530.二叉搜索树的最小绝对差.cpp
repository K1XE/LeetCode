/*
 * @lc app=leetcode.cn id=530 lang=cpp
 *
 * [530] 二叉搜索树的最小绝对差
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
    TreeNode* pre = nullptr;
    int diff = INT_MAX;
    int getMinimumDifference(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [cur, visit] = stk.top();
            stk.pop();
            if (visit) 
            {
                if (pre && abs(pre->val - cur->val) < diff) diff = abs(pre->val - cur->val);
                pre = cur;
                continue;
            }
            if (cur->right) stk.emplace(cur->right, 0);
            stk.emplace(cur, 1);
            if (cur->left) stk.emplace(cur->left, 0);
        }
        return diff;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* pre = nullptr;
        int diff = INT_MAX;
        int getMinimumDifference(TreeNode* root) {
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