/*
 * @lc app=leetcode.cn id=226 lang=cpp
 *
 * [226] 翻转二叉树
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
    TreeNode* invertTree(TreeNode* root) {

    }
};
// @lc code=end

// 层序
class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            queue<TreeNode*> q;
            if (root) q.push(root);
            while (q.size())
            {
                int n = q.size();
                while (n --)
                {
                    TreeNode* tmp = q.front();
                    q.pop();
                    swap(tmp->left, tmp->right);
                    if (tmp->left) q.push(tmp->left);
                    if (tmp->right) q.push(tmp->right);
                }
            }
            return root;
        }
    };

// 迭代
class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            stack<pair<TreeNode*, bool>> stk;
            if (root) stk.push({root, 0});
            while (stk.size())
            {
                auto tmp = stk.top();
                stk.pop();
                if (tmp.second)
                {
                    swap(tmp.first->left, tmp.first->right);
                    continue;
                }
                if (tmp.first->right) stk.push({tmp.first->right, 0});
                if (tmp.first->left) stk.push({tmp.first->left, 0});
                stk.push({tmp.first, 1});
            }
            return root;
        }
    };

// dfs
class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            if (! root) return nullptr;
            dfs(root);
            return root;
        }
    private:
        void dfs(TreeNode* n)
        {
            if (! n) return;
            swap(n->left,n->right);
            dfs(n->left);
            dfs(n->right);
        }
    };
