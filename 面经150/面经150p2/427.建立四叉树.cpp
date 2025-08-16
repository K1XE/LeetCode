/*
 * @lc app=leetcode.cn id=427 lang=cpp
 *
 * [427] 建立四叉树
 */
class Node {
    public:
        bool val;
        bool isLeaf;
        Node* topLeft;
        Node* topRight;
        Node* bottomLeft;
        Node* bottomRight;
        
        Node() {
            val = false;
            isLeaf = false;
            topLeft = nullptr;
            topRight = nullptr;
            bottomLeft = nullptr;
            bottomRight = nullptr;
        }
        
        Node(bool _val, bool _isLeaf) {
            val = _val;
            isLeaf = _isLeaf;
            topLeft = nullptr;
            topRight = nullptr;
            bottomLeft = nullptr;
            bottomRight = nullptr;
        }
        
        Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
            val = _val;
            isLeaf = _isLeaf;
            topLeft = _topLeft;
            topRight = _topRight;
            bottomLeft = _bottomLeft;
            bottomRight = _bottomRight;
        }
    };
// @lc code=start
#pragma once
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#define ALL(v) v.begin(), v.end()
#define For(i, _) for (int i = 0, i##end = _; i < i##end; ++i)
#define FOR(i, _, __) for (int i = _, i##end = __; i < i##end; ++i)
#define Rep(i, _) for (int i = (_); i >= 0; --i)
#define REP(i, __, _) for (int i = (__), i##end = _; i >= i##end; --i)
typedef long long ll;
typedef unsigned long long ull;
#define V vector
#define pb push_back
#define pf push_front
#define qb pop_back
#define qf pop_front
#define eb emplace_back
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define fi first
#define se second
const int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
const int inf = 0x3f3f3f3f;
const ll infl = 0x3f3f3f3f3f3f3f3fll;
const int mod = 1e9 + 7;
template <class T>
inline bool ckmin(T &x, const T &y) { return x > y ? (x = y, true) : false; }
template <class T>
inline bool ckmax(T &x, const T &y) { return x < y ? (x = y, true) : false; }
int init = []()
{ ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();

/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        int ok = isQuadTree(grid);
        int l = grid.size();
        if (ok == 0) return new Node(0, 1, nullptr, nullptr, nullptr, nullptr);
        else if (ok == 1) return new Node(1, 1, nullptr, nullptr, nullptr, nullptr);
        else if (ok == 2) {
            int mid = l / 2;
            V<V<int>> tl(mid, V<int>(mid)), tr(mid, V<int>(mid)), bl(mid, V<int>(mid)), br(mid, V<int>(mid));
            FOR(i, 0, mid) FOR(j, 0, mid) tl[i][j] = grid[i][j];
            FOR(i, 0, mid) FOR(j, mid, l) tr[i][j - mid] = grid[i][j];
            FOR(i, mid, l) FOR(j, 0, mid) bl[i - mid][j] = grid[i][j];
            FOR(i, mid, l) FOR(j, mid, l) br[i - mid][j - mid] = grid[i][j];
            return new Node(1, 0, construct(tl), construct(tr), construct(bl), construct(br));
        }
        return NULL;
    }
    int isQuadTree(V<V<int>>& grid) {
        int l = grid.size();
        int s = 0;
        FOR(i, 0, l) s += accumulate(ALL(grid[i]), 0);
        if (s == l * l) return 1;
        else if (s == 0) return 0;
        else return 2;
    }
};
// @lc code=end

