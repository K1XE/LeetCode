/*
 * @lc app=leetcode.cn id=110 lang=cpp
 *
 * [110] 平衡二叉树
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
    bool isBalanced(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        unordered_map<TreeNode*, int> height;
        if (root) stk.push({root, 0});
        while (stk.size())
        {
            auto tmp = stk.top();
            stk.pop();
            if (tmp.second)
            {
                if (abs(height[tmp.first->left] - height[tmp.first->right]) > 1) return 0;
                height[tmp.first] = max(height[tmp.first->left], height[tmp.first->right]) + 1;
                continue;
            }
            stk.push({tmp.first, 1});
            if (tmp.first->right) stk.push({tmp.first->right, 0});
            if (tmp.first->left) stk.push({tmp.first->left, 0});
        }
        return 1;
    }

};
// @lc code=end

class Solution {
    public:
        bool isBalanced(TreeNode* root) {
            if (height(root) == -1) return 0;
            else return 1;
        }
    private:
        int height(TreeNode* n)
        {
            if (! n) return 0;
            int l = height(n->left);
            if (l == -1) return -1;
            int r = height(n->right);
            if (r == -1) return -1;
            if (abs(l - r) > 1) return -1;
            int maxD = max(l, r) + 1;
            return maxD;
        }
    };

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        stack<TreeNode*> stk;
        if (root) stk.push(root);
        while (stk.size())
        {
            TreeNode* tmp = stk.top();
            stk.pop();
            if (abs(getDepth(tmp->left) - getDepth(tmp->right)) > 1) return 0;
            if (tmp->left) stk.push(tmp->left);
            if (tmp->right) stk.push(tmp->right); 
        }
        return 1;
    }
private:
    int getDepth(TreeNode* n)
    {
        stack<pair<TreeNode*, bool>> stk;
        if (n) stk.push({n, 0});
        int d = 0;
        int maxD = 0;
        while (stk.size())
        {
            auto tmp = stk.top();
            stk.pop();
            if (tmp.second)
            {
                d --;
                continue;
            }
            d ++;
            maxD = max(maxD, d);
            stk.push({tmp.first, 1});
            if (tmp.first->right) stk.push({tmp.first->right, 0});
            if (tmp.first->left) stk.push({tmp.first->left, 0});
            
        }
        return maxD;
    }
};