s = [int(x) for x in str(int(input().strip()))]
sum_s = sum(s)
for i in range(len(s)):
    for j in range(9, s[i] - 1, -1):
        if (sum_s - s[i] + j) % 3 == 0 and s[i] != j:
            s[i] = j
            print(*s, sep="")
            exit()
for i in range(len(s) - 1, -1, -1):
    for j in range(s[i], -1, -1):
        if (sum_s - s[i] + j) % 3 == 0 and s[i] != j:
            s[i] = j
            print(*s, sep="")
            exit()
