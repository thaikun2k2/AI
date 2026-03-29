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

###### Class Father
class sinhvien():
    def __init__(self, hoten, m_sv):
        self.name = hoten
        self.msv = m_sv
    def diem_tb(self, *a):
        if len(a) == 0:
            dtb = 0
        else:
            tong = 0
            for i in a:
                tong += i
            dtb = tong/len(a)
        return dtb
    
###### Class Child kế thừa từ Class Father + phần của riêng nó
class sinhvien_db(sinhvien):
    def __init__(self, hoten, m_sv, bithday, gioi_tinh):
        super().__init__(hoten, m_sv) ##Kế thừa phần __init__ của class cha
        self.birthday = bithday
        self.gender = gioi_tinh
    def diem_tb(self, *a):
        return super().diem_tb(*a) ##Kế thừa phần diem_tb của class cha
    

    def diemtong(self, *a):
        tong = 0
        for i in a:
            tong += i
        return tong 
    
#################Kế thừa trong OOP (Inheritance)-------------------------------##################   


