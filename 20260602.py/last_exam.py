c={1,2,3}
d={3,4,5}
try:
    print(c+d)
except TypeError:
    print("c,d는 집합입니다!")
    print(c | d)