n, k = input().split()
n = int(n)
k = int(k)

arr = list(map(int,input().split()))
bitarr = []
for i in range(n):
    bitarr.append(0)

def Try(i):
    for j in range(2):
        bitarr[i] = j
        if i == n-1:
            sum = 0
            B = []
            for i in range(n):
                if bitarr[i] == 1:
                    B.append(arr[i])
                    sum += arr[i]
                if sum == k:
                    print(B)
        else:
            Try(i+1)

Try(0)
