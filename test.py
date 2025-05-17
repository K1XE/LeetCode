
def solve(n):
    if n % 2 == 1 and n % 3 == 1 and n % 4 == 1 and n % 6 == 1 and n % 11 == 0:
        return True
    else: return False

for i in range(201, -1, -1):
    if (solve(i)):
        print(i)
        break
    