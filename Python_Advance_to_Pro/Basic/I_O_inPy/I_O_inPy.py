###

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


fread = open("I_O_inPy/Eg.txt", "r")
# print(fread)
# print(fread.read(), "\n") ## read tất cả file

## đọc n ký tự trong file 
# print(fread.read(30))## read 30 ký tự

## bỏ trống n sẽ đọc đến hết
print(fread.read(10), "\n") # đọc 10 ký tự đầu
print(fread.read())## đọc từ vị trí vừa đọc đến hết

