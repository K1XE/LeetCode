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
class Solution {
    public:
        int minXor(vector<int>& nums, int k) {
            int n = nums.size();
            vector<int> px(n + 1, 0);
            for (int i = 0; i < n; ++i) {
                px[i + 1] = px[i] ^ nums[i];
            }
            auto check = [&](int limit) -> bool {
                vector<int> dp(n + 1, inf);
                dp[0] = 0;
                for (int i = 1; i <= n; ++i) {
                    for (int j = i - 1; j >= 0; --j) {
                        int segXor = px[i] ^ px[j];
                        if (segXor <= limit) {
                            ckmin(dp[i], dp[j] + 1);
                        }
                    }
                }
                return dp[n] <= k;
            };
            int l = 0, r = (1 << 30) - 1, res = r;
            while (l <= r) {
                int mid = (l + r) >> 1;
                if (check(mid)) {
                    res = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            return res;
        }
    };