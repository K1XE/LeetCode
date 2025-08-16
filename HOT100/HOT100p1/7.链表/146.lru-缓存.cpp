/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
struct Node
{
    int key;
    int val;
    Node* next;
    Node* prev;
    Node(int _key, int _val) : key(_key), val(_val), next(nullptr), prev(nullptr) {}
};
class LRUCache {
public:
    LRUCache(int c) {
        dummy->next = dummy;
        dummy->prev = dummy;
        _c = c;
    }
    
    int get(int key) {
        Node* node = this->get_node(key);
        return node ? node->val : -1;
    }
    
    void put(int key, int value) {
        Node* node = this->get_node(key);
        if (node)
        {
            node->val = value;
            this->remove(node);
            this->push_front(node);
            return;
        }
        Node* tmp = new Node(key, value);
        this->push_front(tmp);
        hash[key] = tmp;
        if (hash.size() > _c)
        {
            Node* back = dummy->prev;
            this->remove(back);
            hash.erase(back->key);
            delete back;
        }
    }
private:
    int _c;
    Node* dummy = new Node(0, 0);
    unordered_map<int, Node*> hash;
    void remove(Node* n)
    {
        n->next->prev = n->prev;
        n->prev->next = n->next;
    }
    void push_front(Node* n)
    {
        n->prev = dummy;
        n->next = dummy->next;
        n->prev->next = n;
        n->next->prev = n;
    }
    Node* get_node(int key)
    {
        auto it = hash.find(key);
        if (it == hash.end())
        {
            return NULL;
        }
        Node* node = it->second;
        this->remove(node);
        this->push_front(node);
        return node;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

