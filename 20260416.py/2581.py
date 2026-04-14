import math 
def isPrime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
m=int(input())
n=int(input())
prime=[]
for i in range(m, n+1):
    if isPrime(i):
        prime.append(i)
if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))