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

# class sinhvien_nam():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#     def xinchao(self):
#         print(f"Xin chào, tôi là sinh viên nam {self.name} với mã sinh viên {self.msv}")
    
# class sinhvien_nu():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#     def xinchao(self):
#         print(f"Xin chào, tôi là sinh viên nữ {self.name} với mã sinh viên {self.msv}")



# ###Gọi hàm đa hình
# #def xinchao_dahinh(sinhvien_nu):sinhvien_nu.xinchao()
# def xinchao_dahinh(sinhvien_nam):sinhvien_nam.xinchao()


################# Đa hình trong OOP (Polymorphism)-------------------------------##################    


################# Trừu tượng trong OOP (Abstraction)-------------------------------##################    
## Trừu tượng là một khái niệm trong OOP cho phép chúng ta tạo ra các lớp trừu tượng (abstract class) và các phương thức trừu tượng (abstract method). Lớp trừu tượng là một lớp không thể được khởi tạo trực tiếp, mà chỉ có thể được kế thừa bởi các lớp con. Phương thức trừu tượng là một phương thức không có phần thân, mà chỉ có định nghĩa, và phải được triển khai trong các lớp con.
## Abstract class cách dùng:
# ko phải để tạo object(đối tượng)
# mà để định nghĩa "khung" , ép buộc class con phải 

from abc import ABC, abstractmethod
###### Class Father
class sinhvien(ABC):

    @abstractmethod
    def thong_tin(self):
        pass


class sinhvien_db(sinhvien):

    def __init__(self, hoten, m_sv):
        self.name = hoten
        self.msv = m_sv

    def thong_tin(self):
        return f'Thông tin sinh viên 1 là:\n- Full name: {self.name}\n- mã sinh viên là: {self.msv}\n'









################# Trừu tượng trong OOP (Abstraction)-------------------------------##################    
