/*
 * @lc app=leetcode.cn id=104 lang=cpp
 *
 * [104] 二叉树的最大深度
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
    int maxDepth(TreeNode* root) {
        queue<TreeNode*> q;
        int depth = 0;
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
            }
            depth ++;
        }
        return depth;
    }
};
// @lc code=end
class Solution {
    public:
        int maxDepth(TreeNode* root) {
            if (! root) return 0;
            return dfs(root, 0);
        }
    private:
        int dfs(TreeNode* n, int depth)
        {
            if (! n) return depth;
            int maxD = max(dfs(n->left, depth + 1), dfs(n->right, depth + 1));
            return maxD;
        }
    };
