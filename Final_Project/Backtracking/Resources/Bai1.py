n = int(input())
a = []
for i in range(n):
    a.append(0)

def printA(arr):
    for i in arr:
        print(i, end='')
    print()

def Try(i):
    for j in range(2):
        a[i] = j
        if i==n-1:
            printA(a)
        else:
            Try(i+1)

Try(0)