/*
 * @lc app=leetcode.cn id=236 lang=cpp
 *
 * [236] 二叉树的最近公共祖先
 */
#include "tools.h"
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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        auto dfs = [&](auto&& self, TreeNode* n) -> TreeNode*
        {
            if (n == p || n == q || ! n) return n;
            TreeNode* l = self(self, n->left);
            TreeNode* r = self(self, n->right);
            if (l && r) return n;
            else if (l && ! r) return l;
            else if (! l && r) return r;
            else return NULL;
        };
        return dfs(dfs, root);
    }
};
// @lc code=end

