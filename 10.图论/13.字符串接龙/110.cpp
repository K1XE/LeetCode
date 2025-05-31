#pragma once
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#define ALL(v) v.begin(), v.end()
#define For(i, _) for (int i = 0, i##end = _; i < i##end; ++i)
#define FOR(i, _, __) for (int i = _, i##end = __; i < i##end; ++i)
#define Rep(i, _) for (int i = (_) - 1; i >= 0; --i)
#define REP(i, _, __) for (int i = (__) - 1, i##end = _; i >= i##end; --i)
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
int n;
string sta, eds;

int main() {
    cin >> n;
    cin >> sta >> eds;
    unordered_set<string> ss;
    For(i, n){
        string str;
        cin >> str;
        ss.insert(str);
    }
    queue<string> q;
    unordered_map<string, int> vis;
    q.push(sta);
    vis[sta] = 1;
    while (q.size())
    {
        string s = q.front();q.pop();
        int steps = vis[s];
        For(i, s.size()){
            string tmp = s;
            For(j, 26){
                tmp[i] = j + 'a';
                if (tmp == eds) {
                    cout << steps + 1 << endl;
                    return 0;
                }
                if (ss.count(tmp) && vis.find(tmp) == vis.end()) {
                    q.push(tmp);
                    vis[tmp] = steps + 1;
                }
            }
        }
    }
    cout << 0;
    return 0;
}