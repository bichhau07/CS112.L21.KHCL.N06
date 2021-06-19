# Nhóm 3 - 4/10
def Help(List,n):
    if len(List) == 0:
        print("False")
        return
    try:
            for j in range(i+1, n):

                for k in range(i, j+1):
                    print(List[k], end=" ")
                print("\n", end="")
                A.append(List)
    except:
        print("\nAn exception occurred")

def Len(A):
    return len(A)

Temp=int(input())
input_string = input()
List=input_string.split()
A = []

for i in range(len(List)):
    List[i] = int(List[i])%1000000007
Help(List,Temp)
print(Len(A))