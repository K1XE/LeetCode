#include <bits/stdc++.h>
using namespace std;
class KMP{
    public:
        void getNext(string& s, vector<int>& next)
        {
            int j = 0; // ǰ׺ĩβ
            next[0] = 0;
            for (int i = 1; i < s.size(); i ++ )
            {
                while (j > 0 && s[j] != s[i]) j = next[j - 1]; // �ҵ����ͬǰ��׺
                if (s[j] == s[i]) j ++; // �ҵ�����ͬǰ��׺
                next[i] = j; // ��ǰ׺���ȸ���next
            }
        }
        bool isSubstr(string s, string t)
        {
            vector<int> next(t.size());
            getNext(t, next);
            int i = 0, j = 0;
            while (i < s.size())
            {
                if (s[i] == s[j])
                {
                    i ++, j ++;
                    if (j == t.size()) return 1;
                }
                else
                {
                    if (j > 0) j = next[j - 1]; // ��t��ʼƥ���λ��
                    else i ++; // û����ͬǰ��׺ i����
                }
            }
            return 0;
        }
};