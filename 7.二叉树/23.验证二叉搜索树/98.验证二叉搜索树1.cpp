/*
 * @lc app=leetcode.cn id=98 lang=cpp
 *
 * [98] 验证二叉搜索树
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
    long long pre = LLONG_MIN;
    bool isValidBST(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                if (node->val <= pre) return 0;
                pre = node->val;
                continue;
            }
            if (node->right) stk.emplace(node->right, 0);
            stk.emplace(node, 1);
            if (node->left) stk.emplace(node->left, 0);
        }
        return 1;
    }
};
// @lc code=end

class Solution {
    public:
        long long pre = LLONG_MIN;
        bool isValidBST(TreeNode* root) {
            if (! root) return 1;
            bool b1 = isValidBST(root->left);
            if (root->val <= pre) return 0;
            pre = root->val;
            bool b2 = isValidBST(root->right);
            return b1 && b2;
        }
    };


    class Solution {
        public:
            long long pre = LLONG_MIN;
            bool isValidBST(TreeNode* root) {
                return dfs(root, LLONG_MIN, LLONG_MAX);
            }
        private:
            bool dfs(TreeNode* n, long long min, long long max)
            {
                if (! n) return 1;
                if (n->val >= max || n->val <= min) return 0;
                bool b1 = dfs(n->left, min, n->val);
                bool b2 = dfs(n->right, n->val, max);
                return b1 && b2;
            }
        };