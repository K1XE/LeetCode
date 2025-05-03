/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
struct Node
{
    int key, val;
    Node *next, *prev;
    Node(int _key, int _val) : key(_key), val(_val), next(nullptr), prev(nullptr) {}
};
class LRUCache {
public:
    LRUCache(int capacity) {
        dummy->next = dummy;
        dummy->prev = dummy;
        _c = capacity;
    }
    
    int get(int key) {
        Node* tmp = get_node(key);
        return tmp ? tmp->val : -1;
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
        Node* tmp = new Node(key, value);
        hash[key] = tmp;
        push_front(tmp);
        if (hash.size() > _c)
        {
            Node *u = dummy->prev;
            remove(u);
            hash.erase(u->key);
            delete u;
        }
    }
private:
    int _c;
    Node* dummy = new Node(0, 0);
    unordered_map<int, Node*> hash;
    void remove(Node *n)
    {
        n->next->prev = n->prev;
        n->prev->next = n->next;
    }
    void push_front(Node *n)
    {
        n->next = dummy->next;
        n->prev = dummy;
        n->next->prev = n;
        dummy->next = n;
    }
    Node* get_node(int key)
    {
        auto it = hash.find(key);
        if (it == hash.end()) return NULL;
        Node* n = it->second;
        remove(n);
        push_front(n);
        return n;
    }

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

