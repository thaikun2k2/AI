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
## Vai trò của Class Father sẽ:
# Định nghĩa khung chung
# Không chứa logic cụ thể (hoặc chứa ít)
# Ép class con phải làm theo khung chung đó
# lưu ý: class cha ko tạo object(đối tượng)

## Vai trò của Class Children sẽ:
# Kế thừa khung chung từ class cha
# Triển khai logic cụ thể cho các phương thức trừu tượng


## Trừu tượng = chỉ định nghĩa “cái cần làm”, không nói “làm như thế nào”.

# from abc import ABC, abstractmethod
# ###### Class Father
# class sinhvien(ABC):

#     @abstractmethod
#     def thong_tin(self):
#         pass


# class sinhvien_db(sinhvien):

#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv

#     def thong_tin(self):
#         return f'Thông tin sinh viên 1 là:\n- Full name: {self.name}\n- mã sinh viên là: {self.msv}\n'

################# Trừu tượng trong OOP (Abstraction)-------------------------------##################    



################# Advanced (Nâng cao)-------------------------------##################    


### Magic method (phương thức đặc biệt)------ 
##Magic Methods = cách bạn “điều khiển hành vi của object trong Python”


# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#     def __str__(self):
#         return f"Xin chào, tôi là sinh viên {self.name} với mã sinh viên {self.msv}" # định nghĩa phương thức __str__ để trả về tên khi in object

### Magic method (phương thức đặc biệt)------ 




### class method & static method ------ 
# 👉 “Khác nhau giữa classmethod và staticmethod là gì?????????”
# Class method nhận class (cls) và thường dùng để thao tác với class-level data,
# trong khi static method không phụ thuộc vào class hay instance,
# chỉ là một hàm tiện ích đặt trong class để tổ chức code tốt hơn.



# @classmethod

# Nhận tham số đầu tiên là cls (lớp hiện tại)
# Thích hợp để thao tác dữ liệu cấp lớp (class variables)
# Có thể tạo instance từ class, kế thừa đúng (subclass vẫn xử lý cls chính xác)

# @staticmethod

# Không nhận self hoặc cls (không “biết” class/instance)
# Cơ bản chỉ là hàm tiện ích đặt trong class để tổ chức code
# Không truy cập thuộc tính class hoặc instance trừ khi truyền rõ ràng



# class sinhvien():
#     count = 0
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#         sinhvien.count += 1 # tăng biến đếm mỗi khi có instance mới được tạo ra

#     @classmethod
#     def get_count(cls): # class method get_count để đếm số lượng đối tượng đã được tạo ra từ class sinhvien
#         return cls.count # trả về số lượng instance đã được tạo ra
    

#     @staticmethod   
#     def is_valid_msv(msv): # static method is_valid_msv để kiểm tra xem mã sinh viên có hợp lệ hay không
#         return isinstance(msv, int) and msv > 0 # kiểm tra xem mã sinh viên có phải là số nguyên dương hay không
    
### class method & static method ------ 

### cách dùng property(getter/setter) ----------
## dùng property để tạo getter và setter cho thuộc tính __score,
#  giúp chúng ta có thể truy cập và thay đổi giá trị của __score một cách an toàn từ bên ngoài class,
# đồng thời kiểm tra tính hợp lệ của giá trị khi thiết lập điểm mới.
## lưu ý: khi dùng property phải có đủ cả getter và setter,
#  nếu thiếu một trong hai thì sẽ ko thể truy cập hoặc thay đổi giá trị của thuộc tính đó từ bên ngoài class được nữa
# class sinhvien():
#     def __init__(self, hoten, m_sv):
#         self.name = hoten
#         self.msv = m_sv
#         self.__score = 0
    
#     @property
#     def score(self):
#         return self.__score # getter method để truy cập giá trị của thuộc tính __score từ bên ngoài class
    
#     @score.setter
#     def score(self, value):
#         if 0 <= value <= 10: # setter method để thiết lập giá trị cho thuộc tính __score từ bên ngoài class, đồng thời kiểm tra xem giá trị có hợp lệ hay không
#             self.__score = value
#         else:
#             print("Điểm phải nằm trong khoảng từ 0 đến 10.")


### cách dùng property(getter/setter) ----------




# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, amount):
#         if not isinstance(amount, (int, float)):
#             raise TypeError("Balance phải là số")
#         if amount < 0:
#             raise ValueError("Số dư không thể âm")

#         else:
#             self.__balance = amount




################# Advanced (Nâng cao)-------------------------------##################    







