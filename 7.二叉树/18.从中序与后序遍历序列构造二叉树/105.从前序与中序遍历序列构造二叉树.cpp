/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (! preorder.size() || ! inorder.size()) return nullptr;
        return dfs(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }
private:
    TreeNode* dfs(vector<int>& pre, vector<int>& in, int lpr, int rpr, int lin, int rin)
    {
        if (lpr > rpr) return nullptr;
        int tmp = pre[lpr];
        TreeNode* root = new TreeNode(tmp);
        if (lpr == rpr) return root;
        int mid;
        for (mid = lin; mid <= rin; mid ++ )
        {
            if (in[mid] == tmp) break;
        }
        int lin_s = lin, lin_e = mid - 1;
        int rin_s = mid + 1, rin_e = rin;
        lpr ++;
        int lpr_s = lpr, lpr_e = lpr + lin_e - lin_s;
        int rpr_s = lpr_e + 1, rpr_e = rpr;
        root->left = dfs(pre, in, lpr_s, lpr_e, lin_s, lin_e);
        root->right = dfs(pre, in, rpr_s, rpr_e, rin_s, rin_e);
        return root;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
            if (! preorder.size() || ! inorder.size()) return nullptr;
            return dfs(preorder, inorder);
        }
    private:
        TreeNode* dfs(vector<int>& pre, vector<int>& in)
        {
            if (! pre.size()) return nullptr;
            int tmp = pre[0];
            TreeNode* root = new TreeNode(tmp);
            if (pre.size() == 1) return root;
            int mid;
            for (mid = 0; mid < in.size(); mid ++)
            {
                if (in[mid] == tmp) break;
            }
            vector<int> lin(in.begin(), in.begin() + mid);
            vector<int> rin(in.begin() + mid + 1, in.end());
            pre.erase(pre.begin());
            vector<int> lpr(pre.begin(), pre.begin() + lin.size());
            vector<int> rpr(pre.begin() + lin.size(), pre.end());
            root->left = dfs(lpr, lin);
            root->right = dfs(rpr, rin);
            return root;
        }
    };