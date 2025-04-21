/*
 * @lc app=leetcode.cn id=111 lang=cpp
 *
 * [111] 二叉树的最小深度
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
    int minDepth(TreeNode* root) {
        return dfs(root);
    }
private:
    int dfs(TreeNode* n)
    {
        if (! n) return 0;
        int l = dfs(n->left);
        int r = dfs(n->right);
        if (n->left && ! n->right) return l + 1;
        else if (n->right && ! n->left) return r + 1;
        else return min(l, r) + 1;
    }
};
// @lc code=end


class Solution {
    public:
        int minDepth(TreeNode* root) {
            dfs(root, 1);
            return root ? res : 0;
        }
    private:
        int res = INT_MAX;
        void dfs(TreeNode* n, int d)
        {
            if (! n) return;
            if (! n->left && ! n->right)
            {
                res = min(res, d);
                return;
            }
            dfs(n->left, d + 1);
            dfs(n->right, d + 1);
        }
    };


class Solution {
    public:
        int minDepth(TreeNode* root) {
            queue<TreeNode*> q;
            int level = 0;
            if (root) q.emplace(root);
            while (q.size())
            {
                level ++;
                int n = q.size();
                while (n --)
                {
                    TreeNode* tmp = q.front();
                    q.pop();
                    if (! tmp->left && ! tmp->right) return level;
                    if (tmp->left) q.emplace(tmp->left);
                    if (tmp->right)  q.emplace(tmp->right);
                }
            }
            return level;
        }
    };