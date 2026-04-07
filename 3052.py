u=[]
for i in range(10):
    x=int(input())
    result= x%42
    u.append(result)
print(len(set(u)))