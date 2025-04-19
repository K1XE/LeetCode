/*
 * @lc app=leetcode.cn id=111 lang=cpp
 *
 * [111] 二叉树的最小深度
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
    int minDepth(TreeNode* root) {
        queue<TreeNode*> q;
        if (root) q.push(root->left), q.push(root->right);
        else return 0;
        int depth = 1;
        while (q.size())
        {
            int n = q.size();
            bool flag = 0;
            while (n --)
            {
                TreeNode* tmp = q.front();
                q.pop();
                if (tmp == NULL) continue;
                else if (tmp != NULL && !flag) flag = 1, depth ++;
                if (!tmp->left && !tmp->right) return depth;
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
            }
        }
        return depth;
    }
};
// @lc code=end

class Solution {
    public:
        int minDepth(TreeNode* root) {
            if (! root) return 0;
            return dfs(root);
        }
    private:
        int dfs(TreeNode* n)
        {
            if (! n) return 0;
            if (! n->left) return dfs(n->right) + 1;
            if (! n->right) return dfs(n->left) + 1;
            return min(dfs(n->left), dfs(n->right)) + 1;
        }
    };