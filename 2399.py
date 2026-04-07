n = int(input())
a=list(map(int,input().split()))
a.sort()
total=0
p=0
for i in range(n):
    total+= a[i]*i-p
    p+=a[i]
print(total*2)