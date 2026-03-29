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
    

# class sinhvien_db:
#     def __init__(self, hoten, m_sv, bithday, gioi_tinh):
#         self.name = hoten
#         self.msv = m_sv
#         self.birthday = bithday
#         self.gender = gioi_tinh
#     def diem_tb(self, *a):
#         if len(a) == 0:
#             dtb = 0
#         else:
#             tong = 0
#             for i in a:
#                 tong += i
#             dtb = tong/len(a)
#         return dtb
#     def diemtong(self, *a):
#         tong = 0
#         for i in a:
#             tong += i
#         return tong 





#################Kế thừa trong OOP (Inheritance)-------------------------------##################   

# ###### Class Father
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
    
# ###### Class Child kế thừa từ Class Father + phần của riêng nó
# class sinhvien_db(sinhvien):
#     def __init__(self, hoten, m_sv, bithday, gioi_tinh):
#         super().__init__(hoten, m_sv) ##Kế thừa phần __init__ của class cha
#         self.birthday = bithday
#         self.gender = gioi_tinh
#     def diem_tb(self, *a):
#         return super().diem_tb(*a) ##Kế thừa phần diem_tb của class cha
    

#     def diemtong(self, *a):
#         tong = 0
#         for i in a:
#             tong += i
#         return tong 
    
#################Kế thừa trong OOP (Inheritance)-------------------------------##################   


#################Đóng gói trong OOP (Encapsulation)-------------------------------##################    



## đang chưa đóng gói
# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#         self.diem_max = 10
#         self.diem_min = 0

#     def diem_tb(self, *a):
#         if len(a) == 0:
#             dtb = 0
#         else:
#             tong = 0
#             for i in a:
#                 if self.diem_min <= i <= self.diem_max:      
#                     tong += i
#                 else:
#                     print(f"Điểm {i} không hợp lệ, điểm phải nằm trong khoảng từ {self.diem_min} đến {self.diem_max}. Điểm này sẽ bị bỏ qua.")
#                     return
#             dtb = tong/len(a)
#         return dtb



########### Đóng gói (Encapsulation)
## Khi đóng gói thì sẽ ko thể thay đổi đc giá trị từ bên ngoài class, chỉ có thể thay đổi giá trị của diem_max thông qua phương thức của class sinhvien
## Điều này giúp bảo vệ dữ liệu và đảm bảo tính toàn vẹn của đối tượng sinh

### Sau khi đã đóng gói

# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#         self.__diem_max = 10
#         self.__diem_min = 0

#     def diem_tb(self, *a):
#         if len(a) == 0:
#             dtb = 0
#         else:
#             tong = 0
#             for i in a:
#                 if self.__diem_min <= i <= self.__diem_max:      
#                     tong += i
#                 else:
#                     print(f"Điểm {i} không hợp lệ, điểm phải nằm trong khoảng từ {self.__diem_min} đến {self.__diem_max}. Điểm này sẽ bị bỏ qua.")
#                     return
#             dtb = tong/len(a)
#         return dtb

###ko thể can thiệp trục tiếp từ bên ngoài class để thay đổi



# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#         self.__diem_max = 10
#         self.__diem_min = 0

#     def diem_tb(self, *a):
#         if len(a) == 0:
#             dtb = 0
#         else:
#             tong = 0
#             for i in a:
#                 if self.__diem_min <= i <= self.__diem_max:      
#                     tong += i
#                 else:
#                     print(f"Điểm {i} không hợp lệ, điểm phải nằm trong khoảng từ {self.__diem_min} đến {self.__diem_max}. Điểm này sẽ bị bỏ qua.")
#                     return
#             dtb = tong/len(a)
#         return dtb
#     def set_diem_max(self, new_diem_max):
#         self.__diem_max = new_diem_max




#################Đóng gói trong OOP (Encapsulation)-------------------------------##################    




################# Đa hình trong OOP (Polymorphism)-------------------------------##################    





















################# Đa hình trong OOP (Polymorphism)-------------------------------##################    
