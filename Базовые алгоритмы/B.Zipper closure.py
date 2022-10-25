n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = []
for i in zip(a, b):
    m += i
print(*m)
