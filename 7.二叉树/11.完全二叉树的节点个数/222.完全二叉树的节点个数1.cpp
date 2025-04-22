/*
 * @lc app=leetcode.cn id=222 lang=cpp
 *
 * [222] 完全二叉树的节点个数
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
    int countNodes(TreeNode* root) {
        return dfs(root);
    }
private:
    int dfs(TreeNode* n)
    {
        if (! n) return 0;
        int l = 0, r = 0;
        TreeNode* nl = n->left;
        TreeNode* nr = n->right;
        while (nl)
        {
            nl = nl->left;
            l ++;
        }
        while (nr)
        {
            nr = nr->right;
            r ++;
        }
        if (l == r)
        {
            return (2 << l) - 1;
        }
        return dfs(n->left) + dfs(n->right) + 1;
    }
};
// @lc code=end

