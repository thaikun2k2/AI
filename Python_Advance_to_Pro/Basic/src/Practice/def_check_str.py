
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



# ## viết hàm copy 1 chuỗi cho trc vs số lần copy cho trc
# a, b = str(input("Nhập vào 1 chuỗi và số lần in ra cách nhau bởi dấu ,: ")).split(",")

# c = int(b)
# def copy_lan(a, c):
#     ketqua = ""
#     for i in range(c):
#         ketqua = ketqua + a
#     return ketqua

# x = copy_lan(a, c)
# print(x)






# in số lần xuất hiện số trg 1 list



# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9]

# s = 2
# def dem_phtu(s,l):
#     d = 0
#     for i in l:
#         if l[i] == s:
#             d += 1
#     return d

# f = dem_phtu(s, l)
# print(f)



#copy n ký tự đầu của str lên n lần

# string1, s2, copy1 = str(input(" Nhập vào string, số ký tự đầu, số lần copy : ")).split(",")
# s1 = int(s2)
# copy = int(copy1)
# x = string1[0:copy] * s1
# print(x)



string1, s2, copy1 = str(input(" Nhập vào string, số ký tự đầu, số lần copy : ")).split(",")

s1 = int(s2)
copy = int(copy1)

def copy_kytu(string1, copy):
    global s1
    ketqua = ""
    for i in range(copy):
        ketqua += string1[0:s1]
    return ketqua

xx = copy_kytu(string1, copy)

print(xx)