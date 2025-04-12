#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;
    string s;
    for (auto c : str)
    {
        if (c - '0' >=0 && c - '0' <=9)
        {
            s.append("number");
        }
        else
        {
            s += c;
        }
    }
    cout << s << endl;
    return 0;
}