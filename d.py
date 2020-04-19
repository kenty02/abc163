from itertools import combinations
n, k = map(int, input().split())
li = []
for a in range(n+1):
    li.append(a)
ari = []
while k != n+2:
    comb = combinations(li, k)
    for combi in comb:
        item = [k, combi]
        if item not in ari:
            ari.append([k, combi])
    k += 1
print(len(ari))
