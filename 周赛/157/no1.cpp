#include "tools.h"
class Solution
{
public:
    bool isPrime(long long n)
    {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        for (long long i = 5; i * i <= n; i += 6)
        {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }
    long long sumOfLargestPrimes(string s)
    {
        int n = s.size();
        string pack = "";
        unordered_set<long long> ss;
        for (int i = 0; i < n; i++)
        {
            string tmp = "";
            for (int j = i; j < n; j++)
            {
                tmp.push_back(s[j]);
                if (tmp[0] == '0')
                    continue;
                long long num = stoll(tmp);
                if (isPrime(num))
                {
                    ss.insert(num);
                }
            }
        }
        vector<long long> res(ss.begin(), ss.end());
        ranges::sort(res, greater<>());
        long long o = 0;
        for (int i = 0; i < min((int)res.size(), 3); i ++ )
        {
            o += res[i];
        }
        return o;
    }
};