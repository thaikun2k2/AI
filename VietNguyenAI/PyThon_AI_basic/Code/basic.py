import math

from numpy.random import choice

"kiểu dữ liệu basic"
"int : số nguyên"
"float : số thực"
"str : lưu văn bản"
"bool : True or False"
"""
a = float(input())
b = float(input())
c = float(input())
if a == 0:
    print(c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("pt vo nghiêm")
    elif delta == 0:
        print(-b/2/a)
    else:
        print((-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a))

month = int(input())
year = int(input())

if 1>= month or month >= 12:
    print("lỗi không có tháng nào")
else:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        print("đây là năm nhuận")
        if month == 2:
            print("số ngày trong tháng 2 là 29")
    else:
        if month == 2:
            print("số ngày trong tháng là 28")

    if month == 3 or month == 1 or month == 8 or month == 5 or month == 7 or month == 12 or month == 10:
        print("số day trong tháng này là 31")
    else:
        print("day on month == 30")

tien = 100
while tien > 0 :
    tien = tien -10
    print(tien)

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(len(a)):
    print(a[i])

s = "abcd"
print(s[0])
z0 = s[0]
print(id(s))
print(id(z0))


chr(mã ascii) -> ob kiểu str
repr(ob) -> ob kiểu str
str(ob) -> ob kiểu str
object thuộc lớp str

s = 65
'mã ascii'
z = chr(s)
print(s)
print(type(s))
print(id(s))
print(z)
print(type(z))
print(id(z))

'đối tượng kiểu chuỗi -> str'
z = repr(s)
print(type(z))
print(z)

'đối tượng bất kỳ  -> str'
z = str(s)
print(type(z))
print(z)

"""
