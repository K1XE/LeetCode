/*
 * @lc app=leetcode.cn id=1865 lang=cpp
 *
 * [1865] 找出和为指定值的下标对
 */

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

class FindSumPairs {
public:
    unordered_map<int, int> hash;
    V<int> v1, v2;
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        v1 = nums1, v2 = nums2;
        for (auto x : v2) hash[x] ++;
    }
    
    void add(int index, int val) {
        int tmp = v2[index];
        auto it = hash.find(tmp);
        if (--(it->second) == 0) hash.erase(it);
        v2[index] += val;
        hash[v2[index]] ++;
    }
    
    int count(int tot) {
        int res = 0;
        for (auto x : v1) {
            int tar = tot - x;
            if (hash.find(tar) != hash.end()) res += hash[tar];
        }
        return res;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
// @lc code=end

