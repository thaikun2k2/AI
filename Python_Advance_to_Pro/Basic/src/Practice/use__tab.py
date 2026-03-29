# print("2 năm nghĩa vụ tạm xa nhà")
# print("\tKhi về phố thị nở đầy hoa")
# print("\t\tNgười yêu ra đón cùng con nhỏ")
# print("Chào chú đi con ...bạn má nè!")

#print("2 năm nghĩa vụ tạm xa nhà", "\n\tKhi về phố thị nở đầy hoa", "\n\t\tNgười yêu ra đón cùng con nhỏ", "\nChào chú đi con ...bạn má nè!")




# from cmath import pi
# import sys
# print(sys.version[0:7])


# n = int(input("Bán kính hình tròn: "))

# tron = pi * (n**2)
# print("Diện tích hình tròn là:", tron)



#chuyển đổi dạng ngày tháng năm

# n = (30, 3, 2026)
# print("{}/{}/{}".format(n[0], n[1], n[2]))
# print("%i/%i/%i" % (30, 3, 2026))



# n = input("Nhập số nguyên cách nhau bởi dấu , là: ")
# a = n.split(",")
# lists = []
# tuples = ()
# sets = {}
# for i in a:
#     lists.append(str(i))
#     tuples = tuple(lists)
# print(lists)
# print(tuples)



# files = input("nhập vào tên file: ")
# a = files.split(".")
# print("đuôi mở rộng là: ", a[-1])

# ## cách xem chức năng của lệnh là: "lệnh.__doc___"
# print(abs.__doc__)
# print(str.__doc__)



# import calendar
# y = int(input("nhập vào năm: "))
# m = int(input("Nhập vào tháng: "))
# lichthang = calendar.month(y, m)
# print(lichthang)

# # nhập vào năm: 2026
# # Nhập vào tháng: 3
# #      March 2026
# # Mo Tu We Th Fr Sa Su
# #                    1
# #  2  3  4  5  6  7  8
# #  9 10 11 12 13 14 15
# # 16 17 18 19 20 21 22
# # 23 24 25 26 27 28 29
# # 30 31



# #in số ngày giữa 2 sự kiện
# import datetime
# sk1 = datetime.date(2026,4,30)
# sk2 = datetime.date(2026,3,30)
# delta = sk1 - sk2
# print(delta)


