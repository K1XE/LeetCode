/*
 * @lc app=leetcode.cn id=968 lang=cpp
 *
 * [968] 监控二叉树
 */
#include "tools.h"
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
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
    int minCameraCover(TreeNode* root) {
        int res = 0;
        auto dfs = [&](auto&& self, TreeNode* n) -> int
        {
            if (! n) return 2;
            int l = self(self, n->left);
            int r = self(self, n->right);
            if (l == 2 && r == 2) return 0;
            if (l == 0 || r == 0) 
            {
                res ++;
                return 1;
            }
            if (l == 1 || r == 1) return 2;
            return -1;
        };
        if (dfs(dfs, root) == 0) res ++;
        return res;
    }
};
// @lc code=end

