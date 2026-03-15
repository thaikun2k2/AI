
# ===============================
# LƯU Ý VỀ HÀM (FUNCTION) TRONG PYTHON
# ===============================

# | Nội dung | Cú pháp / Ví dụ | Ghi chú |
# |----------|-----------------|--------|
# | Khai báo hàm | def ten_ham(): | dùng từ khóa def |
# | Tham số (parameter) | def add(a, b): | a, b là tham số |
# | Gọi hàm | add(2,3) | truyền đối số |
# | Giá trị trả về | return a + b | return kết thúc hàm |
# | Hàm không return | def hello(): print("Hi") | mặc định trả về None |
# | Tham số mặc định | def hello(name="Python"): | dùng khi không truyền |
# | Keyword argument | hello(name="An") | truyền theo tên |
# | Positional argument | hello("An") | truyền theo vị trí |
# | *args | def sum_all(*args): | nhận nhiều đối số dạng tuple |
# | **kwargs | def info(**kwargs): | nhận nhiều key=value dạng dict |
# | Hàm trong hàm | def outer(): | nested function |
# | Lambda function | lambda x: x*2 | hàm 1 dòng |
# | Docstring | """Mô tả hàm""" | dùng để giải thích hàm |
# | Type hint | def add(a:int,b:int)->int | gợi ý kiểu dữ liệu |
# | Scope biến | local / global | phạm vi biến |
# | global keyword | global x | sửa biến global |
# | nonlocal keyword | nonlocal x | sửa biến ngoài hàm con |
# | Hàm là object | f = add | có thể gán cho biến |
# | Hàm làm tham số | map(func, list) | truyền hàm vào hàm |
# | Decorator | @decorator | mở rộng chức năng hàm |


##y = abs(x) trả outcome là y là trị tuyệt đối của x

from math import * ## lấy tất cả thư viện math

# def tri_tuỵet_doi(x):
#     if x >= 0:
#         y = x
#     else:
#         y = -x
#     return y
# def print_vision(z):
#     print(z)
#     return

# x = -5
# y = tri_tuỵet_doi(x)
# print_vision(f'giá trị tuyệt đối của x là: {y}')



# #
# #a = hypot(3,4) a# cạnh huyền của tam giác vuông
# b = 3
# c = 4

# def canh_huyen_tamgiac(b, c):
#     a = sqrt(b*b + c*c)
#     return a

# a = canh_huyen_tamgiac(b, c)
# print(f'cạnh huyền là: {a}')


### tham số truyền: 

##Eg1: truyền theo kiểu giá trị
# def hamxx(v):
#     v=3 # immutable ô nhớ số 1
#     return v
# m = 2 #mutable ô nhớ số 2
# y = hamxx(m)
# print("giá trị hàm xx trả về là:", y)#=3 ko có j thay đổi

# print("giá trị của m là:", m)#2 ko thay đổi

#Eg2:  truyền theo kiểu tham chiếu đến ô nhớ đó
# u = 3
# def hamxx(t):
#     t.append(u) ## thêm giá trị vào ô nhớ mutable
#     return t
# n = [1, 2] # ô nhớ số 1
# l = hamxx(n) #truyền n vào hàm có phương thức append thêm vào ô nhớ trg hàm
# print("giá trị hàm xx trả về là:", l)#giá trị đã thay đổi

# print("giá trị của n là:", n)#giá trị đã thay đổi



#required argument(bắt buộc đúng theo thứ tự tham số truyền vào)

# #required: quan trọng ở thứ tự 
# def ham(v, k):
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# k = [6, 7]
# y = ham(m, k)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi

#argument: ko quan tâm đến thứ tự gàn thêm tên argument

# def ham(v, k):
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# kk = [6, 7]
# y = ham(k=kk, v = m)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi


##đefault argument: khi gọi hàm nếu ko truyền sẽ lấy giá trị mặc định

# def ham(v, k = 3):#k = 3 là default
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# kk = [6, 7]
# y = ham( v = m)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi



###########----def có đối số thay đổi, hàm nặc danh, biến cục bộ, biến toàn cục
# def so_max(a, b):## định nghĩa có 2 số
#     if a > b:
#         smax = a
#     else:
#         smax = b
#     return smax
# #y = so_max(3, 4,) ##ko thể dựa vào so_max(3, 4, 5) vì theo định nghĩa chỉ đưa vào 2 số thôi

# y = so_max(3, 4) ##ko thể dưad vào so_max(3, 4, 5) vì theo định nghĩa chỉ đưa vào 2 số thôi
# print("number max: ", y)


# def ham(var1, var2 = 2, *var3)
# var1:required argument
# phải truyền giá trị khi gọi hàm, nếu không sẽ báo lỗi
# var2: default argument
# nếu khi gọi hàm không truyền giá trị thì Python sẽ dùng giá trị mặc định (ở đây là 2)

# *var3: variable length argument
# cho phép truyền nhiều đối số tùy ý
# các giá trị truyền vào sẽ được lưu dưới dạng tuple


# def so_max(a, b, *c):## định nghĩa c là 1 đối số có số lượng phần tử thay đổi vì có " * "
# #c là tuple có nhiều PhTu ở bên trong 0 - n
#     if a > b:
#         smax = a
#     else:
#         smax = b
#     for i in c:
#         if i > smax:
#             smax = i

#     return smax

# y = so_max(3, 4, 5, 6, 7) ##vẫn đc
# print("number max: ", y)


################ Hàm nặc danh = Anonymous Functions
#lambda[arg1[,arg2,.....argn]]:expression
#can có nhiều argument, ko thể chứa nhiều biểu thức or nhiều lệnh, chỉ chứa 1 biểu thức duy nhất

# #eg
# def tong(a, b, c):
#     t = a + b + c
#     return t
# tong1 = lambda a, b, c: a +b +c
# y = tong(3, 4, 5)
# print(f'tổng hàm là: {y}')
# z = tong1(3, 4, 5)
# print(f'tổng hàm nặc danh là: {z}')

# tong2 = lambda a, b, c: a +b +c
# print(f'tổng hàm nặc danh là: {tong2(1, 2, 3)}')

# a, b là đối số truyền vào, not variable
# t là 1 biến, variable - toàn cục: global variable

# def tong (a, b):
#     # t là 1 biến, variable - toàn cục: global variable
#     t = a + b
#     print(f'biến cục bộ: {t}')
#     return t

# y = tong (1, 9)
# print("tong 2 so là : ", y)
# t=5 #t toàn cục
# print("biến toàn cục:", t) #ko liên quan đến t trg hàm tong(a, b)


#############Hàm đệ quy
## thay vì trả về 1 giá trị thì đệ quy trả về 1 lời gọi lại chính nó nhưng mức độ đơn giản hơn lặp lại đến khi đạt trạng thái đơn giản nhất
#phải có điều kiện dừng
#ưu điểm: gọn hơn, nhược điểm: khó theo dõi logic, khó gỡ rối, tốn bộ nhớ

# #eg: giai thừa n
# # import sys
# # sys.setrecursionlimit(5000)
# def giai_thua(n):
#     if n == 1:
#         return 1#trả về giá trị khi trả về giá trị thì nó sẽ dừng
#     else:
#         return n*giai_thua(n - 1)#trả về lời gọi chính bản thân hàm này
    
# y = giai_thua(3)
# #y = giai_thua(1000)#ko thực hiện đc vì quá tốn bộ nhớ
# #để thức hiện đc cần thiết lập bộ nhớ = câu lệnh sau:
# # import sys
# # sys.setrecursionlimit(5000)
# print("giai thừa của n là: ",y)
