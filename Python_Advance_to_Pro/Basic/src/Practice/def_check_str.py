
# # Bước 1: lấy 2 ký tự đầu ra
# # Bước 2: Kiểm tra xem 2 ký tự đó có phải là is hay ko?
# # bước 3: ko phải thì thêm is vào trc, phải thì in ra chuỗi s




# def new_string(s):
#     if s[:2] == "is":
#         s = s
#     else:
#         s = "is" + s
#     return s

# s = "marry"
# s1 = new_string(s)

# print(s1)



## viết hàm copy 1 chuỗi cho trc vs số lần copy cho trc
a, b = str(input("Nhập vào 1 chuỗi và số lần in ra cách nhau bởi dấu ,: ")).split(",")

c = int(b)
def copy_lan(a, c):
    ketqua = ""
    for i in range(c):
        ketqua = ketqua + a
    return ketqua

x = copy_lan(a, c)
print(x)
