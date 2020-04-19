n, m = map(int, input().split())
a = map(int, input().split())
c = 0
for b in a:
    c += b
if n - c < 0:
    print(-1)
else:
    print(n-c)
