/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */
#include "tools.h"
// @lc code=start
class Trie {
private:
    bool isEnd;
    Trie *nxt[26];
public:
    Trie() {
        isEnd = 0;
        memset(nxt, 0, sizeof(nxt));
    }
    
    void insert(string word) {
        Trie *node = this;
        for (auto& ch : word)
        {
            if (node->nxt[ch - 'a'] == NULL) node->nxt[ch - 'a'] = new Trie();
            node = node->nxt[ch - 'a'];
        }
        node->isEnd = 1;
    }
    
    bool search(string word) {
        Trie *node = this;
        for (auto& ch : word)
        {
            node = node->nxt[ch - 'a'];
            if (node == NULL) return 0;
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        Trie *node = this;
        for (auto& ch : prefix)
        {
            node = node->nxt[ch - 'a'];
            if (node == NULL) return 0;
        }
        return 1;
    }

};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

