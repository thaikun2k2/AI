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
sv2 = sinhvien("Nguyen Van B", 654321)
sv3 = sinhvien("Nguyen Van C", 111111)
sv4 = sinhvien("Nguyen Van D", 222222)

x = sv1.diem_tb(6, 7, 8, 9, 10)
y = sv2.diem_tb(5, 6, 7, 8, 9)
z = sv3.diem_tb(4, 5, 6, 7, 8)
w = sv4.diem_tb(3, 4, 5, 6, 7)


# print(sv1.name)
# print(sv1.msv)
print(f'Thông tin sinh viên 1 là: {sv1.name} có mã sinh viên là: {sv1.msv}')
print("Điểm trung bình của sinh viên 1 là: ", x)
print(f'Thông tin sinh viên 2 là: {sv2.name} có mã sinh viên là: {sv2.msv}')
print("Điểm trung bình của sinh viên 2 là: ", y)
print(f'Thông tin sinh viên 3 là: {sv3.name} có mã sinh viên là: {sv3.msv}')
print("Điểm trung bình của sinh viên 3 là: ", z)
print(f'Thông tin sinh viên 4 là: {sv4.name} có mã sinh viên là: {sv4.msv}')
print("Điểm trung bình của sinh viên 4 là: ", w)


