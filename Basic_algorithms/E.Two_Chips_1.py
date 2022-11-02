def two_chips(n, m, x):
    left = 0
    right = n - 1
    while left < right:
        current_sum = m[left] + m[right]
        if current_sum == x:
            return m[left], m[right]
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    return [None]

n = int(input())
m = list(map(int, input().split()))
x = int(input())
print(*two_chips(n, m, x))
