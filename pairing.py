month=int(input())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
start=4
for i in range(month-1):
    start += days[i]
start = start%7
print("일 월 화 수 목 금 토")
print("   "* start, end="")
for i in range(1, days[month-1]+1):
    print(f"{i:2}", end=" ")
    if (i + start)% 7 ==0:
        print()