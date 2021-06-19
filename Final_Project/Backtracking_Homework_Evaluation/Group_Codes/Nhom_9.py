# Nhóm 9 - 10/10
n = int(input())
l = list(map(int,input().split()))
arr = []
bitarray = []
A = []

for i in range(n):
  bitarray.append(0)

def Try(i):
  if n < 2:
    print("False")
  else:
    for j in range(2):
      bitarray[i] = j
      if i == n-1:
        status = 0
        a = []
        for i in range(n):
          if (bitarray[i]==1 and i-1 >=0 and bitarray[i-1]==1):
            status = 1
          if bitarray[i] == 1:
            a.append(l[i])
        if status == 1:
            A.append(bitarray)
      else:
        Try(i+1)

Try(0)
for i in range(len(arr)):
  print(*arr[i],sep=" ")

print(len(A))