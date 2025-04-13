#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int m, n;
const int N = 105;
int a[N][N], h[N][1], l[1][N];
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i ++ )
    {
        int sumh = 0;
        for (int j = 0; j < m; j ++ )
        {
            cin >> a[i][j];
            sumh += a[i][j];
        }
        if (i == 0) h[i][0] = sumh;
        else h[i][0] = h[i - 1][0] + sumh;
    }
    for (int j = 0; j < m; j ++ )
    {
        int suml = 0;
        for (int i = 0; i < n; i ++ )
        {
            suml += a[i][j];
        }
        if (j == 0) l[0][j] = suml;
        else l[0][j] = l[0][j - 1] + suml;
    }
    int minDiff1 = INT32_MAX, minDiff2 = INT32_MAX;
    for (int i = 0; i < n; i ++ )
    {
        int p1 = h[i][0];
        int p2 = h[n - 1][0] - h[i][0];
        int diff = abs(p1 - p2);
        minDiff1 = min(minDiff1, diff);
    }
    for (int j = 0; j < m; j ++ )
    {
        int p1 = l[0][j];
        int p2 = l[0][m - 1] - l[0][j];
        int diff = abs(p1 - p2);
        minDiff2 = min(minDiff2, diff);
    }
    cout << min(minDiff1, minDiff2) << endl;
    return 0;
}