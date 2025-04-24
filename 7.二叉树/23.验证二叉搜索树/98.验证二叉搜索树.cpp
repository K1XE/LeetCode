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
    TreeNode* pre = nullptr;
    bool isValidBST(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [cur, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                if (pre && pre->val >= cur->val) return 0;
                pre = cur;
                continue;
            }
            if (cur->right) stk.emplace(cur->right, 0);
            stk.emplace(cur, 1);
            if (cur->left) stk.emplace(cur->left, 0);
        }
        return 1;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* pre = nullptr;
        bool isValidBST(TreeNode* root) {
            TreeNode* pre = nullptr;
            return dfs(root);
        }
    private:
        bool dfs(TreeNode* n)
        {
            if (! n) return 1;
            bool b1 = dfs(n->left);
            if (pre && n->val <= pre->val) return 0;
            pre = n;
            bool b2 = dfs(n->right);
            return b1 && b2;
        }
    };


// wo shi sha bi ^ ^
class Solution {
    public:
        bool isValidBST(TreeNode* root) {
            return dfs(root, LLONG_MIN, LLONG_MAX);
        }
    private:
        bool dfs(TreeNode* n, long long min, long long max)
        {
            if (! n) return 1;
            if (n->val <= min || n->val >= max) return 0;
            bool b1 = dfs(n->left, min, n->val);
            bool b2 = dfs(n->right, n->val, max);
            return b1 & b2;
        }
    };


    class Solution {
        public:
            long long minVal = LLONG_MIN;
            bool isValidBST(TreeNode* root) {
                return dfs(root);
            }
        private:
            bool dfs(TreeNode* n)
            {
                if (! n) return 1;
                bool b1 = dfs(n->left);
                if (n->val > minVal) minVal = n->val;
                else return 0;
                bool b2 = dfs(n->right);
                return b1 && b2;
            }
        };