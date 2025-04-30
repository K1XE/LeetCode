/*
 * @lc app=leetcode.cn id=106 lang=cpp
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return dfs(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1);
    }
private:
    TreeNode* dfs(vector<int>& in, vector<int>& p, int inl, int inr, int pl, int pr)
    {
        if (pl > pr) return NULL;
        int tmp = p[pr];
        TreeNode* u = new TreeNode(tmp);
        if (pl == pr) return u;
        int mid = 0;
        for (int i = inl; i <= inr; i ++ )
        {
            if (in[i] == tmp)
            {
                mid = i;
                break;
            }
        }
        int linl = inl, linr = mid - 1, rinl = mid + 1, rinr = inr;
        int lpl = pl, lpr = lpl + linr - linl, rpl = lpl + linr - linl + 1, rpr = -- pr;
        u->left = dfs(in, p, linl, linr, lpl, lpr);
        u->right = dfs(in, p, rinl, rinr, rpl, rpr);
        return u;
    }
};
// @lc code=end

