max_val=0
index=0
for i in range(1,10):
    n = int(input())
    if n>max_val:
        max_val=n
        index=i
print(max_val)
print(index)