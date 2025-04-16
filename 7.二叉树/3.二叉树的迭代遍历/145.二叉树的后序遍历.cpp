/*
 * @lc app=leetcode.cn id=145 lang=cpp
 *
 * [145] 二叉树的后序遍历
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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> stk;
        vector<int> res;
        if (! root) return res;
        stk.push(root);
        while (stk.size())
        {
            TreeNode* p = stk.top();
            stk.pop();
            res.push_back(p->val);
            if (p->left) stk.push(p->left);
            if (p->right) stk.push(p->right);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
// @lc code=end
// sol 1
class Solution {
    public:
        vector<int> postorderTraversal(TreeNode* root) {
            stack<TreeNode*> stk;
            vector<int> res;
            TreeNode* cur = root;
            TreeNode* lastVisit = nullptr; // 用于判断右子树是否访问过
            while (stk.size() || cur)
            {
                if (cur)
                {
                    stk.push(cur);
                    cur = cur->left;
                }
                else
                {
                    TreeNode* tmp = stk.top();
                    if (! tmp->right || lastVisit == tmp->right)
                    {
                        res.push_back(tmp->val);
                        stk.pop();
                        lastVisit = tmp;
                    }
                    else
                    {
                        cur = tmp->right;
                    }
                }
            }
            return res;
        }
    };
// sol 2
class Solution {
    public:
        vector<int> postorderTraversal(TreeNode* root) {
            stack<TreeNode*> stk1, stk2;
            vector<int> res;
            if (!root) return res;
            stk1.push(root);
            // 根 -> 右 -> 左 {stk1}
            // 左 -> 右 -> 根 {stk2}
            while (stk1.size()) 
            {
                TreeNode* p = stk1.top();
                stk1.pop();
                stk2.push(p);
                if (p->left) stk1.push(p->left);
                if (p->right) stk1.push(p->right);
            }
            while (stk2.size())
            {
                res.push_back(stk2.top()->val);
                stk2.pop();
            }
            return res;
        }
    };
// sol 3
class Solution {
    public:
        vector<int> postorderTraversal(TreeNode* root) {
            vector<int> res;
            dfs(root, res);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& res)
        {
            if (n == nullptr) return;
            dfs(n->left, res);
            dfs(n->right, res);
            res.push_back(n->val);
        }
    };
