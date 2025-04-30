/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
 */
#include <bits/stdc++.h>
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
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return dfs(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }
private:
    TreeNode* dfs(vector<int>& preorder, vector<int>& inorder, int prel, int prer, int inl, int inr)
    {
        if (prel > prer) return NULL;
        int tmp = preorder[prel];
        TreeNode* u = new TreeNode(tmp);
        if (prel == prer) return u;
        int mid = 0;
        for (int i = inl; i <= inr; i ++ )
        {
            if (inorder[i] == tmp)
            {
                mid = i;
                break;
            }
        }
        int linl = inl, linr = mid - 1, rinl = mid + 1, rinr = inr;
        int lprel = ++ prel, lprer = lprel + linr - linl, rprel = lprel + linr - linl + 1, rprer = prer;
        u->left = dfs(preorder, inorder, lprel, lprer, linl, linr);
        u->right = dfs(preorder, inorder, rprel, rprer, rinl, rinr);
        return u;
    }
};
// @lc code=end

