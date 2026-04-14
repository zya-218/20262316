student=[("Junyeong", 20153253, 4.2),
         ("Yeongjae", 20153180, 3.7),
         ("Chaeyeoung", 20153250, 4.5)
]
print("before sorted:",student)
sort_by_id=sorted(student, key=lambda x : x[1])
print("sort by id:", sort_by_id)
sort_by_grade=sorted(student, key=lambda x : x[2])
print("sort by grade:", sort_by_grade)