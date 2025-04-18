/*
 * @lc app=leetcode.cn id=101 lang=cpp
 *
 * [101] 对称二叉树
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
    bool isSymmetric(TreeNode* root) {
        if (! root) return 1;
        return dfs(root->left, root->right);
    }
private:
    bool dfs(TreeNode* l, TreeNode* r)
    {
        if (!l && !r) return 1;
        else if (!l && r) return 0;
        else if (l && !r) return 0;
        else if (l->val != r->val) return 0;
        bool out = dfs(l->left, r->right);
        bool in = dfs(l->right, r->left);
        bool isSame = out & in;
        return isSame;
    }
};
// @lc code=end

// stack
class Solution {
    public:
        bool isSymmetric(TreeNode* root) {
            if (! root) return 1;
            stack<TreeNode*> stk;
            stk.push(root->left), stk.push(root->right);
            while (stk.size())
            {
                TreeNode* tr = stk.top(); stk.pop();
                TreeNode* tl = stk.top(); stk.pop();
                if (!tr && !tl) continue;
                if (!tr || !tl || (tr->val != tl->val)) return 0;
                stk.push(tl->left); stk.push(tr->right);
                stk.push(tl->right); stk.push(tr->left);
            }
            return 1;
        }
    };

// queue
class Solution {
    public:
        bool isSymmetric(TreeNode* root) {
            if (! root) return 1;
            queue<TreeNode*> q;
            q.push(root->left), q.push(root->right);
            while (q.size())
            {
                TreeNode* tl = q.front(); q.pop();
                TreeNode* tr = q.front(); q.pop();
                if (!tl && !tr) continue;
                if (!tl || !tr) return 0;
                if (tl->val != tr->val) return 0;
                q.push(tl->left); q.push(tr->right);
                q.push(tl->right); q.push(tr->left);
            }
            return 1;
        }
    };

// sb stack
class Solution {
    public:
        bool isSymmetric(TreeNode* root) {
            if (! root) return 1;
            stack<TreeNode*> stkl;
            stack<TreeNode*> stkr;
            stkl.push(root->left), stkr.push(root->right);
            while (stkl.size() && stkr.size())
            {
                TreeNode* tl = stkl.top(); stkl.pop();
                TreeNode* tr = stkr.top(); stkr.pop();
                if (!tl && !tr) continue;
                if (!tl || !tr) return 0;
                if (tr->val != tl->val) return 0;
                stkl.push(tl->left), stkl.push(tl->right);
                stkr.push(tr->right), stkr.push(tr->left);
            }
            return stkl.size() == stkr.size();
        }
    };
