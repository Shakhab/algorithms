def chips(n, a, x):
    m = ''
    for i in range(n - 1):
        for j in range(i + 1, n):
            b = a[i] + a[j]
            if b == x:
                m += str(a[i]) + ' ' + str(a[j])
                return ''.join(m)
    return None

n = int(input())
a = list(map(int, input().strip().split()))
x = int(input())
print(chips(n, a, x))
