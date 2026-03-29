## OOP == ObjectOrientedProgramming
# Lập trình hướng đối tượng (OOP) là phương pháp tổ chức code bằng class (lớp) và object (đối tượng).
# Mỗi object gồm:
# - Thuộc tính (attributes) → dữ liệu
# - Phương thức (methods) → hành vi





"""
class sinhvien:
    def __init__(self, tham_so1, tham_so2,...):
        self.thuoc_tinh1 = tham_so1
        self.thuoc_tinh2 = tham_so2
        ...

    def diem_tb(self, *a):
        khối lệnh
        return diem_tb





"""
##################------------------------------- Class & Object --------------------------------##################
# # # Class & Object
# class Person:
#     def __init__(self, name):
#         self.name = name  # attribute: lưu tên của object

# # tạo object (instance)
# p = Person("Thai")

# # truy cập attribute
# print(p.name)  # output: Thai

# # # 👉 Giải thích:

# # # class = bản thiết kế
# # # object = đối tượng thực tế được tạo từ class
# # # self = đại diện cho chính object đó


##################------------------------------- Class & Object --------------------------------##################



##################------------------------------- Constructor (__init__) --------------------------------##################

# class Student:
#     def __init__(self, name, age):
#         self.name = name   # gán giá trị cho attribute name
#         self.age = age     # gán giá trị cho attribute age

# s = Student("Thai", 22)
# print(s.name)  # Output: Thai
# print(s.age)   # Output: 22



# # # 👉 Giải thích:

# # # __init__ chạy tự động khi tạo object
# # # Dùng để khởi tạo dữ liệu ban đầu cho object
# # # self đại diện cho chính object đó




# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#     def diem_tb(self, *a):
#         if len(a) == 0:
#             dtb = 0
#         else:
#             tong = 0
#             for i in a:
#                 tong += i
#             dtb = tong/len(a)
#         return dtb
# sv1 = sinhvien("Nguyen Van A", 123456)
# sv2 = sinhvien("Nguyen Van B", 654321)
# sv3 = sinhvien("Nguyen Van C", 111111)
# sv4 = sinhvien("Nguyen Van D", 222222)

# x = sv1.diem_tb(6, 7, 8, 9, 10)
# y = sv2.diem_tb(5, 6, 7, 8, 9)
# z = sv3.diem_tb(4, 5, 6, 7, 8)
# w = sv4.diem_tb(3, 4, 5, 6, 7)


# # print(sv1.name)
# # print(sv1.msv)
# print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
# print("Điểm trung bình của sinh viên 1 là: ", x)
# print(f'Thông tin sinh viên 2 là: {sv2.name} có mã sinh viên là: {sv2.msv}')
# print("Điểm trung bình của sinh viên 2 là: ", y)
# print(f'Thông tin sinh viên 3 là: {sv3.name} có mã sinh viên là: {sv3.msv}')
# print("Điểm trung bình của sinh viên 3 là: ", z)
# print(f'Thông tin sinh viên 4 là: {sv4.name} có mã sinh viên là: {sv4.msv}')
# print("Điểm trung bình của sinh viên 4 là: ", w)

##################------------------------------- Constructor (__init__) --------------------------------##################




##### Tính kế thừa trong OOP (Inheritance)
##Class cha (parent class) và class con (child class)
## class con sẽ kế thừa thuộc tính và phương thức của class cha
# khi class con kế thừa từ class cha phải chỉ rõ tên class cha
# class con có thể kế thừa 1 ph hoặc toàn bộ 

## class con có thể thêm thuộc tính và phương thức riêng của mình
# Dùng từ khóa super() để phân biệt tài sản kế thừa và tài sản tự làm ra

##kế thừa cành nhiều càng nhàn nhã

from my_type_OOP import*


### Class Father
sv1 = sinhvien("Nguyen Van A", 123456)
# sv2 = sinhvien("Nguyen Van B", 654321)
# sv3 = sinhvien("Nguyen Van C", 111111)
# sv4 = sinhvien("Nguyen Van D", 222222)

x = sv1.diem_tb(6, 7, 8, 9, 10)
# y = sv2.diem_tb(5, 6, 7, 8, 9)
# z = sv3.diem_tb(4, 5, 6, 7, 8)
# w = sv4.diem_tb(3, 4, 5, 6, 7)


# print(sv1.name)
# print(sv1.msv)
print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
print("Điểm trung bình của sinh viên 1 là: ", x)
# print(f'Thông tin sinh viên 2 là: {sv2.name} có mã sinh viên là: {sv2.msv}')
# print("Điểm trung bình của sinh viên 2 là: ", y)
# print(f'Thông tin sinh viên 3 là: {sv3.name} có mã sinh viên là: {sv3.msv}')
# print("Điểm trung bình của sinh viên 3 là: ", z)
# print(f'Thông tin sinh viên 4 là: {sv4.name} có mã sinh viên là: {sv4.msv}')
# print("Điểm trung bình của sinh viên 4 là: ", w)
print("\n")



### Class con kế thừa từ class cha + phần của riêng nó
svdb1 = sinhvien_db("Nguyen Van A", 123456, "01/01/2000", "Nam")
print(f'Thông tin sinh viên 1 là:\n- Full name: {svdb1.name}\n- mã sinh viên là: {svdb1.msv}\n- ngày sinh là: {svdb1.birthday}\n- giới tính là: {svdb1.gender}')
x = svdb1.diem_tb(6, 7, 8, 9, 10)
print("Điểm trung bình của sinh viên 1 là: ", x)
x1 = svdb1.diemtong(6, 7, 8, 9, 10)
print("Điểm tổng của sinh viên 1 là: ", x1)

















