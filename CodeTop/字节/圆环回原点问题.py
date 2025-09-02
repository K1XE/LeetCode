import sys
def solve(n):
    dp = [[0] * (n + 1) for _ in range(10)]
    dp[0][0] = 1
    for j in range(1, n + 1):
        for i in range(10):
            dp[i][j] = dp[(i - 1) % 10][j - 1] + dp[(i + 1) % 10][j - 1]
    return dp[0][n]

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        tmp = list(map(int, line.split()))
        for x in tmp:
            res = solve(x)
            print(res, end=" ")

if __name__ == "__main__":
    main()

