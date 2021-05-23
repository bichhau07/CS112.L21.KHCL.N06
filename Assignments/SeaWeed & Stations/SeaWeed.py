import sys

def fibo(n):
    if n == 1 or n == 2:
        return 1
    f0 = 1
    f1 = 1
    fn = 2
    for i in range(2, n):
        f0 = f1
        f1 = fn
        fn = f0 + f1
    return fn

while True:
    line = sys.stdin.readline()
    if line == "\n":
        break
    n,k = tuple(map(int, line.split()))
    res = n * fibo(2 * k)
    print(res % 1000000007)
