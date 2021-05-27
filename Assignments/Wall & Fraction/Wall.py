n = int(input())
A = list(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

left = high = min(A)
right = min(A) + max(B)
count = 0

while left <= right:
    mid = (left + right) >> 1
    check = True
    j  = num = 0

    for i in range(n):
        if A[i] >= mid: continue
        
        while (j < m and A[i] + B[j] < mid):    
            j += 1
        
        if j >= m: 
            check = False
            break
        j += 1
        num += 1

    if check:
        high  = mid
        left  = mid + 1
        count = num
    else:
        right = mid - 1

print(high,count)
j = 0
for i in range(n):                           
    if A[i] >= high : continue
    
    while (j < m and A[i] + B[j] < high):
        j += 1
    
    if j >= m: 
        check = False
        break
    print(i+1, j+1)
    j += 1