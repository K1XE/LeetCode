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

TreeNode* delete_this_node1(TreeNode* node)
{
    if (! node) return NULL;
    if (! node->right) return node->left;
    TreeNode* cur = node->right;
    while (cur->left)
    {
        cur = cur->left;
    }
    cur->left = node->left;
    return node->right;
}

TreeNode* delete_this_node2(TreeNode* node, int key)
{
    if (! node) return NULL;
    if (node->val == key)
    {
        if (! node->right) return node->left;
        TreeNode* cur = node->right;
        while (cur->left)
        {
            cur = cur->left;
        }
        swap(cur->val, node->val);
    }
    node->left = delete_this_node2(node->left, key);
    node->right = delete_this_node2(node->right, key);
    return node;
}