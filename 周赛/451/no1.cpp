#include "tools.h"
class Solution {
    public:
        string resultingString(string s) {
            int top = 0;
            int n = s.size();
            for (auto ch : s)
            {
                if (top > 0 && (abs(s[top - 1] - ch) == 1 || (s[top - 1] == 'a' && ch == 'z') || (ch == 'a' && s[top - 1] == 'z')))
                {
                    top --;
                }
                else
                {
                    s[top ++] = ch;
                }
            }
            return s.substr(0, top);
        }
    };