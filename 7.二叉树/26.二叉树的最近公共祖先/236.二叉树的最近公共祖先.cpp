/*
 * @lc app=leetcode.cn id=236 lang=cpp
 *
 * [236] 二叉树的最近公共祖先
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct TreeNode
{
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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<TreeNode*, TreeNode*> parent;
        parent[root] = nullptr;
        stack<TreeNode*> stk;
        stk.emplace(root);
        while (! parent.contains(p) || ! parent.contains(q))
        {
            TreeNode* tmp = stk.top();
            stk.pop();
            if (tmp->right)
            {
                parent[tmp->right] = tmp;
                stk.emplace(tmp->right);
            }
            if (tmp->left)
            {
                parent[tmp->left] = tmp;
                stk.emplace(tmp->left);
            }
        }
        TreeNode* a = p;
        TreeNode* b = q;
        while (a != b)
        {
            a = a ? parent[a] : q;
            b = b ? parent[b] : p;
        }
        return a;
    }
};
// @lc code=end

// sol1
class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            return dfs(root, p, q);
        }
    private:
        TreeNode* dfs(TreeNode* root, TreeNode* p, TreeNode* q)
        {
            if (! root) return nullptr;
            if (root == p || root == q) return root;
            TreeNode* l = dfs(root->left, p, q);
            TreeNode* r = dfs(root->right, p, q);
            if (l && r) return root;
            else if (! l && r) return r;
            else if (l && ! r) return l;
            else return nullptr;
        }
    };

// sol2
class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            stack<TreeNode*> stk1, stk2;
            TreeNode* cur = root;
            TreeNode* pre1 = nullptr;
            while (stk1.size() || cur)
            {
                if (cur)
                {
                    stk1.emplace(cur);
                    if (cur == p) break;
                    cur = cur->left;
                }
                else
                {
                    TreeNode* tmp = stk1.top();
                    if (tmp->right && pre1 != tmp->right)
                    {
                        cur = tmp->right;
                    }
                    else
                    {
                        pre1 = tmp;
                        stk1.pop();
                    }
                }
            }
            cur = root;
            TreeNode* pre2 = nullptr;
            while (stk2.size() || cur)
            {
                if (cur)
                {
                    stk2.emplace(cur);
                    if (cur == q) break;
                    cur = cur->left;
                }
                else
                {
                    TreeNode* tmp = stk2.top();
                    if (tmp->right && pre2 != tmp->right)
                    {
                        cur = tmp->right;
                    }
                    else
                    {
                        pre2 = tmp;
                        stk2.pop();
                    }
                }
            }
            while (stk1.size() > stk2.size()) stk1.pop();
            while (stk2.size() > stk1.size()) stk2.pop();
            while (stk1.top() != stk2.top()) stk1.pop(), stk2.pop();
            return stk1.top();
        }
    };