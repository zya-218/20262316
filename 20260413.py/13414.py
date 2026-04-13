import sys
input = sys.stdin.read
data = input().split()

K = int(data[0]) # Сонгогдох оюутны тоо
L = int(data[1]) # Нийт бүртгүүлсэн хүсэлт

waiting_list = {}

# Оюутнуудын мэдээллийг Dictionary-д хадгалах
for i in range(L):
    student_id = data[i + 2]
    # Хамгийн сүүлийн дарааллыг нь хадгална
    waiting_list[student_id] = i

# Дарааллын дугаараар (i) эрэмбэлэх
sorted_students = sorted(waiting_list.items(), key=lambda x: x[1])

# Зөвхөн эхний K оюутныг хэвлэх
count = 0
for student, index in sorted_students:
    if count < K:
        print(student)
        count += 1
    else:
        break