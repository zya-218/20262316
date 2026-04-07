n=int(input())
for i in range(n):
    s=input()
    count=0
    total=0
    for c in s:
        if c=="O":
            count+=1
            total+=count
        else:
            count=0
    print(total)