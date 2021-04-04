def Remove_Smallest(x,r,arr):
        idx = r.index(x)
        arr.pop(idx)
        r.pop(idx)

def Largest_Mul_Three(arr):
    r = [a % 3 for a in arr]
    s = sum(r) % 3

    if s != 0:
        try:
            Remove_Smallest(s, r, arr)
        except:
            Remove_Smallest(3-s, r, arr)
            Remove_Smallest(3-s, r, arr)

    if len(arr) == 0:
        print("")
    else:
        arr.sort(reverse = True)
        print(*arr,sep="")
        
from sys import stdin

string = list(stdin.readline().strip())

arr = []
for i in string:
    arr.append(int(i))
arr.sort()
Largest_Mul_Three(arr)
