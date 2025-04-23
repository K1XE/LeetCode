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
        if (! inorder.size() || ! postorder.size()) return nullptr;
        return dfs(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1);
    }
private:
    TreeNode* dfs(vector<int>& in, vector<int>& post, int in_s, int in_e, int po_s, int po_e)
    {
        if (po_s > po_e) return nullptr;
        int tmp = post[po_e];
        TreeNode* root = new TreeNode(tmp);
        if (po_s == po_e) return root;
        int mid;
        for (mid = in_s; mid <= in_e; mid ++)
        {
            if (in[mid] == tmp) break;
        }
        int lin_s = in_s, lin_e = mid - 1;
        int rin_s = mid + 1, rin_e = in_e;
        po_e --;
        int lpo_s = po_s, lpo_e = po_s + lin_e - lin_s;
        int rpo_s = lpo_e + 1, rpo_e = po_e;
        root->left = dfs(in, post, lin_s, lin_e, lpo_s, lpo_e);
        root->right = dfs(in, post, rin_s, rin_e, rpo_s, rpo_e);
        return root;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
            if (! inorder.size() || ! postorder.size()) return nullptr;
            return dfs(inorder, postorder);
        }
    private:
        TreeNode* dfs(vector<int>& in, vector<int>& post)
        {
            if (! post.size()) return nullptr;
            int tmp = post[post.size() - 1];
            TreeNode* root = new TreeNode(tmp);
            if (post.size() == 1) return root;
            int mid = 0;
            for (; mid < in.size(); mid ++)
            {
                if (in[mid] == tmp) break;
            }
            vector<int> lin(in.begin(), in.begin() + mid);
            vector<int> rin(in.begin() + mid + 1, in.end());
            post.resize(post.size() - 1);
            vector<int> lpo(post.begin(), post.begin() + lin.size());
            vector<int> rpo(post.begin() + lin.size(), post.end());
            root->left = dfs(lin, lpo);
            root->right = dfs(rin, rpo);
            return root;
        }
    };