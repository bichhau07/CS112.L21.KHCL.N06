# Nhóm 7 - 9/10

n = int(input())

rally = list(map(int, input().split()))
temp = [0 for i in range(n)]
A = []

def print_arr(array):
    for i in array:
        print(i, end = ' ')
    print()

def Try(i,A):
    for j in range(2):
        temp[i] = j
        check = 0
        if i == n-1:
            child_rally = []
            for k in range(n-1):
                if temp[k] == 1 and temp[k+1] == 1:
                    check = 1
                    break
            if check == 1:
                for k in range(n):
                    if temp[k] == 1:
                        child_rally.append(rally[k])
                A.append(child_rally)
        else:
            Try(i+1,A)

Try(0,A)
print(len(A))