def H_index(A):
    A.sort()
    for i, val in enumerate(A):
        res = len(A) - i
        if res <= val:
            return res
    return 0

n = int(input())
A = list(map(int,input().split()))

print(H_index(A))
