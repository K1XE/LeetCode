/*
 * @lc app=leetcode.cn id=100 lang=cpp
 *
 * [100] 相同的树
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return dfs(p, q);
    }
private:
    bool dfs(TreeNode* n1, TreeNode* n2)
    {
        if (!n1 || !n2)
        {
            return n1 == n2;
        }
        return n1->val == n2->val && dfs(n1->left, n2->left) && dfs(n1->right, n2->right);
    }
};
// @lc code=end
class Solution {
    public:
        bool isSameTree(TreeNode* p, TreeNode* q) {
            return dfs(p, q);
        }
    private:
        bool dfs(TreeNode* n1, TreeNode* n2)
        {
            if (!n1 && n2) return false;
            else if (n1 && !n2) return false;
            else if (!n1 && !n2) return true;
            else if (n1->val != n2->val) return false;
            bool l =  dfs(n1->left, n2->left);
            bool r = dfs(n1->right, n2->right);
            return l & r;
        }
    };
