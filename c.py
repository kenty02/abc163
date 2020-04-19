n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for c in a:
    b[c-1] += 1

for bitem in b:
    print(bitem)
