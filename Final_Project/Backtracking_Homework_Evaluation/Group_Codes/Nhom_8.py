# Nhóm - 9/10

n = int(input())
A = list(map(int,input().split(" ")[:n]))
B = []
bitarray=[]

for i in range(n):
    bitarray.append(0)

def Try(i):
    for j in range(2):
        bitarray[i] = j
        if i == n-1:
            check = 0
            b=[]
            for i in range(n):
                if bitarray[i] == 1 and bitarray[i-1] == 1 and i-1>=0:
                    check = 1
                if bitarray[i] == 1:
                    b.append(A[i])
            if check == 1:
                B.append(b)
        else:
            Try(i+1)

Try(0)
print(len(B))