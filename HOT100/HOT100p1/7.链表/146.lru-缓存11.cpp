/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存
 */
#include "tools.h"
// @lc code=start
struct Node
{
    int key, val;
    Node *pre, *nxt;
    Node(int k, int v) : key(k), val(v), pre(nullptr), nxt(nullptr) {}
};
class LRUCache {
public:

    LRUCache(int capacity) {
        dummy->nxt = dummy;
        dummy->pre = dummy;
        _c = capacity;
    }
    
    int get(int key) {
        Node* n = get_node(key);
        return n ? n->val : -1;
    }
    
    void put(int key, int value) {
        Node *n = get_node(key);
        if (n)
        {
            n->val = value;
            remove(n);
            push_front(n);
            return;
        }
        Node *u = new Node(key, value);
        push_front(u);
        hash[key] = u;
        if (hash.size() > _c)
        {
            Node *back = dummy->pre;
            remove(back);
            hash.erase(back->key);
            delete back;
        }
    }
private:
    int _c;
    Node* dummy = new Node(0, 0);
    unordered_map<int, Node*> hash;
    void remove(Node *n)
    {
        n->pre->nxt = n->nxt;
        n->nxt->pre = n->pre;
    }
    void push_front(Node *n)
    {
        n->nxt = dummy->nxt;
        dummy->nxt->pre = n;
        dummy->nxt = n;
        n->pre = dummy;
    }
    Node* get_node(int key)
    {
        auto it = hash.find(key);
        if (it == hash.end())
        {
            return NULL;
        }
        Node *tmp = it->second;
        remove(tmp);
        push_front(tmp);
        return tmp;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

