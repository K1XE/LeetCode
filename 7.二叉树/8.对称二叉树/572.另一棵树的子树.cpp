/*
 * @lc app=leetcode.cn id=572 lang=cpp
 *
 * [572] 另一棵树的子树
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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        int sh = this->len(subRoot);
        return dfs(root, sh, subRoot).second;
    }
private:
    pair<int, bool> dfs(TreeNode* n, int h, TreeNode* subn)
    {
        if (! n) return {0, 0};
        auto l = dfs(n->left, h, subn);
        auto r = dfs(n->right, h, subn);
        if (l.second || r.second) return {0, 1};
        int nh = max(l.first, r.first) + 1;
        return {nh, nh == h && cmp(n, subn)};
    }
    int len(TreeNode* n)
    {
        if (! n) return 0;
        int ll = this->len(n->left);
        int rl = this->len(n->right);
        return max(ll, rl) + 1; 
    }
    bool cmp(TreeNode* n1, TreeNode* n2)
    {
        if (! n1 || ! n2)
        {
            return n1 == n2;
        }
        return n1->val == n2->val && cmp(n1->left, n2->left) && cmp(n1->right, n2->right);
    }
};
// @lc code=end
class Solution {
    public:
        bool isSubtree(TreeNode* root, TreeNode* subRoot) {
            stack<TreeNode*> stk;
            if (root) stk.push(root);
            while (stk.size())
            {
                TreeNode* tmp = stk.top();
                stk.pop();
                if (cmp(tmp, subRoot)) return 1;
                if (tmp->right) stk.push(tmp->right);
                if (tmp->left) stk.push(tmp->left);
            }
            return 0;
        }
    private:
        bool cmp(TreeNode* n1, TreeNode* n2)
        {
            if (! n1 || ! n2)
            {
                return n1 == n2;
            }
            return n1->val == n2->val && cmp(n1->left, n2->left) && cmp(n1->right, n2->right);
        }
    };
