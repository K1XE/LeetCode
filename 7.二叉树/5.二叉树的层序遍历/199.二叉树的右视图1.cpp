/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
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
    vector<int> res;
    vector<int> rightSideView(TreeNode* root) {
        dfs(root, 0);
        return res;
    }
private:
    void dfs(TreeNode* n, int depth)
    {
        if (! n) return;
        if (depth == res.size()) res.emplace_back(n->val);
        dfs(n->right, depth + 1);
        dfs(n->left, depth + 1);
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> rightSideView(TreeNode* root) {
            vector<int> res;
            queue<TreeNode*> q;
            if (root) q.push(root);
            while (q.size())
            {
                int n = q.size();
                while (n --)
                {
                    TreeNode* tmp = q.front();
                    q.pop();
                    if (tmp->left) q.push(tmp->left);
                    if (tmp->right) q.push(tmp->right);
                    if (! n) res.push_back(tmp->val);
                }
            }
            return res;
        }
    };