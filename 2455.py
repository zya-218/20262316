current_people=0
max_people=0
for i in range(4):
    buusn, suusn=map(int,input().split())
    current_people+= suusn-buusn
    if current_people > max_people:
        max_people= current_people
print(max_people)