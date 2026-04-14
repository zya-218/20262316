def hansu(n):
    s=str(n)
    if len(s)<=2:
        return True
    diff=int(s[1])-int(s[0])
    for i in range(1, len(s)-1):
        if int(s[i+1])-int(s[i]) !=diff:
            return False
    return True
n = int(input())
count=0
for i in range(1, n+1):
    if hansu(i):
        count+=1
print(count)