from math import gcd
a, b, c, d = [int(input()) for _ in range(4)]
count = 0
A = a/b
B = c/d

while (A < B):
  count += 1
  a += 1
  b += 1

  m = gcd(a,b)
  a = a // m
  b = b // m
  A = a/b

  if (A == B):
    print(count)
    break

if A != B:
  print(0)