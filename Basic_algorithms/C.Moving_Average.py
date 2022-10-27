n = int(input ())
a = list(map(int, input().split()))
K = int(input())
result = []
current_sum = sum(a[0:K])
result.append(current_sum / K)
for i in range(0, len(a) - K):
    current_sum -= a[i]
    current_sum += a[i+K]
    current_avg = current_sum / K
    result.append(current_avg)
print(" ".join(map(str, result)))
