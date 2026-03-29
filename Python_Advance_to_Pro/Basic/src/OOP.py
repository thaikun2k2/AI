## OOP == ObjectOrientedProgramming
# Lập trình hướng đối tượng (OOP) là phương pháp tổ chức code bằng class (lớp) và object (đối tượng).
# Mỗi object gồm:
# - Thuộc tính (attributes) → dữ liệu
# - Phương thức (methods) → hành vi



from my_type_OOP import*

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




#################Kế thừa trong OOP (Inheritance)-------------------------------##################   


# ##### Tính kế thừa trong OOP (Inheritance)
# ##Class cha (parent class) và class con (child class)
# ## class con sẽ kế thừa thuộc tính và phương thức của class cha
# # khi class con kế thừa từ class cha phải chỉ rõ tên class cha
# # class con có thể kế thừa 1 ph hoặc toàn bộ 

# ## class con có thể thêm thuộc tính và phương thức riêng của mình
# # Dùng từ khóa super() để phân biệt tài sản kế thừa và tài sản tự làm ra

# ##kế thừa cành nhiều càng nhàn nhã

# from my_type_OOP import*


# ### Class Father
# sv1 = sinhvien("Nguyen Van A", 123456)
# # sv2 = sinhvien("Nguyen Van B", 654321)
# # sv3 = sinhvien("Nguyen Van C", 111111)
# # sv4 = sinhvien("Nguyen Van D", 222222)

# x = sv1.diem_tb(6, 7, 8, 9, 10)
# # y = sv2.diem_tb(5, 6, 7, 8, 9)
# # z = sv3.diem_tb(4, 5, 6, 7, 8)
# # w = sv4.diem_tb(3, 4, 5, 6, 7)


# # print(sv1.name)
# # print(sv1.msv)
# print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
# print("Điểm trung bình của sinh viên 1 là: ", x)
# # print(f'Thông tin sinh viên 2 là: {sv2.name} có mã sinh viên là: {sv2.msv}')
# # print("Điểm trung bình của sinh viên 2 là: ", y)
# # print(f'Thông tin sinh viên 3 là: {sv3.name} có mã sinh viên là: {sv3.msv}')
# # print("Điểm trung bình của sinh viên 3 là: ", z)
# # print(f'Thông tin sinh viên 4 là: {sv4.name} có mã sinh viên là: {sv4.msv}')
# # print("Điểm trung bình của sinh viên 4 là: ", w)
# print("\n")



# ### Class con kế thừa từ class cha + phần của riêng nó
# svdb1 = sinhvien_db("Nguyen Van A", 123456, "01/01/2000", "Nam")
# print(f'Thông tin sinh viên 1 là:\n- Full name: {svdb1.name}\n- mã sinh viên là: {svdb1.msv}\n- ngày sinh là: {svdb1.birthday}\n- giới tính là: {svdb1.gender}')
# x = svdb1.diem_tb(6, 7, 8, 9, 10)
# print("Điểm trung bình của sinh viên 1 là: ", x)
# x1 = svdb1.diemtong(6, 7, 8, 9, 10)
# print("Điểm tổng của sinh viên 1 là: ", x1)

#################Kế thừa trong OOP (Inheritance)-------------------------------##################   




#################Đóng gói trong OOP (Encapsulation)-------------------------------##################    






## đang chưa đóng gói

# sv1 = sinhvien("Nguyen Van A", 123456)
# sv1.diem_max = 20
# x = sv1.diem_tb(6, 7, 8, 9, 10, 12)



# print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
# print(x)


## đang ko đc đóng gói vì sv1.diem_max = 20 đã thay đổi đc giá trị của diem_max trong class sinhvien
## dẫn đến việc điểm 12 đã được tính vào điểm trung bình dù nó không hợp lệ (vượt quá điểm tối đa là 10)
## để khắc phục vấn đề này, chúng ta cần đóng gói thuộc tính diem_max


########### Đóng gói (Encapsulation)
## Khi đóng gói thì sẽ ko thể thay đổi đc giá trị từ bên ngoài class, chỉ có thể thay đổi giá trị của diem_max thông qua phương thức của class sinhvien
## Điều này giúp bảo vệ dữ liệu và đảm bảo tính toàn vẹn của đối tượng sinh




# sv1 = sinhvien("Nguyen Van A", 123456)
# sv1.__diem_max = 20 ## thuộc tính đã được đóng gói, không thể can thiệp trực tiếp từ bên ngoài class
# x = sv1.diem_tb(6, 7, 8, 9, 10, 12)



# print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
# print(x)

##Mục đích vc đóng gói là: để bảo vệ 1 số thuộc tính quan trong của đối tượng, tránh việc bị thay đổi giá trị từ bên ngoài class
#  đảm bảo tính toàn vẹn của dữ liệu và giúp kiểm soát cách thức truy cập




# ##sau khi đã thêm biến thay đổi từ bên trong của đóng gói 
# sv1 = sinhvien("Nguyen Van A", 123456)
# #sv1.__diem_max = 20 ## vẫn sẽ ko thay đổi đc

# sv1.set_diem_max(20) ## thay đổi giá trị của diem_max thông qua phương thức set_diem_max của class sinhvien
# x = sv1.diem_tb(6, 7, 8, 9, 10, 12)



# print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
# print(x)

########=====>>>>>>để thay đổi thuộc tính đã đc đóng gói thì phải thay đổi từ bên trong đối tượng
########=====>>>>>>ko thể thay đổi đc từ bên ngoài đối tượng


#################Đóng gói trong OOP (Encapsulation)-------------------------------##################    



################# Đa hình trong OOP (Polymorphism)-------------------------------##################    

###if 2 kiểu type nhưng lại 2 hàm có tên giống nhau thì sẽ xảy ra đa hình, khi đó hàm nào sẽ được gọi sẽ phụ thuộc vào kiểu dữ liệu của đối tượng mà hàm đó được gọi đến
### đa hình giúp cho code linh hoạt hơn, dễ bảo trì hơn và dễ mở rộng hơn

"""
class type1:
    def hamxx():
        chức năng 1
class type2:
    def hamxx():
        chức năng 2

a.hamxx() ===>>> chức năng 1
b.hamxx() ===>>> chức năng 2

### xây dựng hàm 1 hàm chung cho cả a và b :
def hamxx(obj):
    obj.hamxx()
hamxx(a) ===>>> chức năng 1
hamxx(b) ===>>> chức năng 2
## ==>> đây đc gọi là tính đa hình (Polymorphism)
"""


# #from my_type_OOP import*




# sv1 = sinhvien_nam("Nguyen Van A", 123456)
# sv2 = sinhvien_nu("Nguyen Van B", 654321)

# # x = sv1.xinchao()
# # y = sv2.xinchao()


# ### tính đa hình của hàm
# xinchao_dahinh(sv1)
# xinchao_dahinh(sv2)


### =====>>>>>> xây dụng hàm chung cho các kiểu dữ liệu khác nhau thì đc gọi là tính đa hình (Polymorphism)
### lưu ý: là phải cùng tên hàm nhưng chức năng khác nhau


################# Đa hình trong OOP (Polymorphism)-------------------------------##################    


################# Trừu tượng trong OOP (Abstraction)-------------------------------##################    


### Class Father


### Trừu tượng = chỉ định nghĩa “cái cần làm”, không nói “làm như thế nào”.

# svdb1 = sinhvien_db("Nguyen Van A", 123456)
# print(f'{svdb1.thong_tin()}')

################# Trừu tượng trong OOP (Abstraction)-------------------------------##################    




################# Magic method (phương thức đặc biệt)-------------------------------##################    
# ## Magic method là các phương thức đặc biệt được định nghĩa sẵn trong Python, có tên bắt đầu và kết thúc bằng hai dấu gạch dưới (ví dụ: __init__, __str__, __add__, v.v.). Chúng cho phép chúng ta tùy chỉnh hành vi của các đối tượng khi thực hiện các phép toán hoặc khi in đối tượng, v.v. 
# # Ví dụ, phương thức __str__ cho phép chúng ta định nghĩa cách mà đối tượng sẽ được hiển thị khi chúng ta in nó ra
# ## Nếu chúng ta định nghĩa phương thức __str__ trong class sinhvien, thì khi chúng ta in một đối tượng của class sinhvien, Python sẽ tự động gọi phương thức __str__ để lấy chuỗi đại diện cho đối tượng đó và in ra

# # tạo object (instance)
# sv1 = sinhvien("Nguyen Van A", 123456)
# print(sv1)  # do đã định nghĩa __str__ nên khi in object sv1 sẽ gọi đến phương thức __str__ để trả về chuỗi đại diện cho object đó
# # ko thì sẽ có kết quả là: <__main__.sinhvien object at 0x7f8c8c8c8c8c>

################# Magic method (phương thức đặc biệt)-------------------------------##################    































