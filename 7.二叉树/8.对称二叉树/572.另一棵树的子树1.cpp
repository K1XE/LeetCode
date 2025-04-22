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
        int sub_d = getDepth(subRoot);
        return dfs(root, subRoot, sub_d).second;
    }
private:
    int getDepth(TreeNode* n)
    {
        if (! n) return 0;
        int a = getDepth(n->left);
        int b = getDepth(n->right);
        return max(a, b) + 1;
    }
    pair<int, bool> dfs(TreeNode* n1, TreeNode* n2, int sub_d)
    {
        if (! n1) return {0, 0};
        auto l = dfs(n1->left, n2, sub_d);
        auto r = dfs(n1->right, n2, sub_d);
        if (l.second || r.second) return {0, 1};
        int d = max(l.first, r.first) + 1;  
        return {d, d == sub_d && cmp(n1, n2)};
    }
    bool cmp(TreeNode* n1, TreeNode* n2)
    {
        if (! n1 && ! n2) return 1;
        else if (! n1 && n2) return 0;
        else if (n1 && ! n2) return 0;
        else if (n1->val != n2->val) return 0;
        bool b1 = cmp(n1->left, n2->left);
        bool b2 = cmp(n1->right, n2->right);
        return b1 && b2;
    }
};
// @lc code=end

class Solution {
    public:
        bool isSubtree(TreeNode* root, TreeNode* subRoot) {
            int root_d = getDepth(root), sub_d = getDepth(subRoot);
            return dfs(root, subRoot, 1, root_d, sub_d);
        }
    private:
        int getDepth(TreeNode* n)
        {
            if (! n) return 0;
            int a = getDepth(n->left);
            int b = getDepth(n->right);
            return max(a, b) + 1;
        }
        bool dfs(TreeNode* n1, TreeNode* n2, int cur_depth, int root_d, int sub_d)
        {
            if (! n1) return 0;
            if (root_d - cur_depth + 1 < sub_d) return 0;
            if (cmp(n1, n2)) return 1;
            bool b1 = dfs(n1->left, n2, cur_depth + 1, root_d, sub_d);
            bool b2 = dfs(n1->right, n2, cur_depth + 1, root_d, sub_d);
            return b1 || b2;
        }
        bool cmp(TreeNode* n1, TreeNode* n2)
        {
            if (! n1 && ! n2) return 1;
            else if (! n1 && n2) return 0;
            else if (n1 && ! n2) return 0;
            else if (n1->val != n2->val) return 0;
            bool b1 = cmp(n1->left, n2->left);
            bool b2 = cmp(n1->right, n2->right);
            return b1 && b2;
        }
    };