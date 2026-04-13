n=int(input())
books={}
for _ in range(n):
    name=input().strip()
    if name in books:
        books[name]+=1
    else:
        books[name]=1
max_count= max(books.values())
candidates=[]
for name in books:
    if books[name]==max_count:
        candidates.append(name)
candidates.sort()
print(candidates[0])