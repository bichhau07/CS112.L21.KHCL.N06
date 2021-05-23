a, k, b, m, n = list(map(int, input().split()))
left, right = 0, 2 * (n // (a + b)) + 1
while left + 1 < right:
    mid = (left + right) // 2
    x1 = a * (k - 1) * (mid // k) + a * (mid % k)
    x2 = b * (m - 1) * (mid // m) + b * (mid % m) 
    if x1 + x2 >= n:
        right = mid
    else:
        left = mid
print(right)
