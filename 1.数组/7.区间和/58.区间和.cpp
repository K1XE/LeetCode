#include <bits/stdc++.h>
using namespace std;
int n, a, b, sums;
const int N = 1e5 + 10;
int arr[N];
int backup[N];
int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ )
    {
        cin >> arr[i];
        sums += arr[i];
        backup[i] = sums;
    }
    while (cin >> a >> b)
    {
        cout << (a ? (backup[b] - backup[a - 1]) : backup[b]) << endl;
    }
    return 0;
}