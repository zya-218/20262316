n, k=map(int,input().split())
max_n =0
for i in range(1, k+1):
    num = n * i
    rev = int(str(num)[::-1])
    if rev>max_n:
        max_n =rev
print(max_n)