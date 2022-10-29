def chips(n, a, x):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] == x:
                return a[i], a[j]
    return [None]

n = int(input())
a = list(map(int, input().strip().split()))
x = int(input())
print(*chips(n, a, x))

