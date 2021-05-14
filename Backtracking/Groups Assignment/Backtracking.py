def Print(bitarray):
    for i in range(n):
        if bitarray[i]==1:
            print(list0[i],end='')
    print()

def Try(i, A):
    if n==0:
        print('False')
    else:
        for j in range(2):
            bitarray[i]=j
            if i==n-1:
                status=0
                for i in range(1,n):
                    if bitarray[i]==1 and bitarray[i-1]==1:
                        status=1
                if(status):
                    A.append(bitarray)    
            else:
                Try(i+1, A)

def Len(A):
    return len(A)

n = int(input())
list0 = list(map(int,input().split()))
bitarray=[]
A = []

for i in range(n):
    bitarray.append(0)


Try(0, A)
print(Len(A))