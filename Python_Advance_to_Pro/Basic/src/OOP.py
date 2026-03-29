## OOP == ObjectOrientedProgramming


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
sv1 = sinhvien("Nguyen Van A", 123456)


print(sv1.name)
print(sv1.msv)


print(sv1.diem_tb(8, 9, 10))