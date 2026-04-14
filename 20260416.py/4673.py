def d(n):
    return n + sum(map(int,str(n)))
g=set()
for i in range(1,10001):
    g.add(d(i))
for i in range(1,10001):
    if i not in g:
        print(i)