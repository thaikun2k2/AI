###
# hom nay troi nang dep
# kien tri ky luat
# tu ky
# tinh yeu 
# phan boi trung thanh

# ##các cách input
# Input: 
# input()
# Hàm open() : Mở đối tượng file 
# ==>> cho phép đọc, ghi, ... đến file
# #cách thao tác: file --> open() --> file object
# # Name_file_object = open(file_name, access mode, buffering)




# Output print()

#r: read --> only read

# Name_file_object.read(n)
#  --n là số ký tự trong file mình muốn đọc, bỏ trống n sẽ đọc đến hết


fread = open("I_O_inPy/Eg.txt", "r", encoding= "utf-8") ##encoding= "utf-8" cần dùng khi nếu trg file có ký tự tiếng việt sẽ ko đọc đc, và sẽ cần mã hóa về dạng tiếng việt để đọc ra thành công
# # print(fread)
# # print(fread.read(), "\n") ## read tất cả file

# ## đọc n ký tự trong file 
# # print(fread.read(30))## read 30 ký tự

# ## bỏ trống n sẽ đọc đến hết
# print(fread.read(10), "\n") # đọc 10 ký tự đầu

# #Name_file_object.tell() vị trí con trỏ trong file hiện tại ở đâu
# print(fread.tell(), "\n")## vị trí thứ 10 --> trả về vị trí của fill pointer
# #Name_file_object.seek(n) thay đổi vị trí con trỏ hiên tại trong file
# # đưa file pointer về vị trí n
# print(fread.seek(0), "\n")

# print(fread.read(), "\n")## đọc từ vị trí hiện tại đến hết
# Name_file_object.close() đóng file
# fread.close()#đóng file
#eg:
# print(fread.read(), "\n")# do đã đóng file nên sẽ bị lỗi


## bỏ trống n sẽ đọc đến hết
print(fread.read(15), "\n") # đọc 15 ký tự đầu

#Name_file_object.tell() vị trí con trỏ trong file hiện tại ở đâu
print(fread.tell(), "\n")## vị trí thứ 20 --> trả về vị trí của fill pointer do là ký tự tiếng việt
print(fread.read(), "\n")## đọc từ vị trí hiện tại đến hết