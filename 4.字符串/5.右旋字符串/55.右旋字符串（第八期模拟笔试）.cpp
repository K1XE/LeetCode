#include <bits/stdc++.h>
using namespace std;
int main()
{
    int pos;
    cin >> pos;
    string s;
    cin >> s;
    pos = s.size() - pos;
    int l1 = 0, r1 = pos - 1;
    while (l1 < r1)
    {
        swap(s[l1 ++], s[r1 --]);
    }
    l1 = pos, r1 = s.size() - 1;
    while (l1 < r1)
    {
        swap(s[l1 ++], s[r1 --]);
    }
    l1 = 0, r1 = s.size() - 1;
    while (l1 < r1)
    {
        swap(s[l1 ++], s[r1 --]);
    }
    cout << s << endl;
    return 0;
}