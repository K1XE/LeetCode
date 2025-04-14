#include <bits/stdc++.h>
using namespace std;
string s;

void solve ()
{
    cin >> s;
    string res;
    for (auto c : s)
    {
        if (c - '0' >= 0 && c - '0' <= 9)
        {
            res += "number";
        }
        else
        {
            res += c;
        }
    }
    cout << res << endl;
}

int main()
{
    solve();
    return 0;
}