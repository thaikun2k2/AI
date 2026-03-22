###
# hom nay troi nang dep
# kien tri ky luat
# tu ky
# tinh yeu 
# phan boi trung thanh
# hi vong
# tu tuong
# khon canh



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

######## "r" là chỉ đc phép đọc ko đc ghi
#fread = open("I_O_inPy/Eg.txt", "r", encoding= "utf-8") ##encoding= "utf-8" cần dùng khi nếu trg file có ký tự tiếng việt sẽ ko đọc đc, và sẽ cần mã hóa về dạng tiếng việt để đọc ra thành công
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





# hôm nay trời nắng đẹp
# kiên trì kỷ luật
# tự kỷ
# tình yêu 
# phản bội trung thành
# hi vọng
# tư tưởng
# khốn cảnh


# ## bỏ trống n sẽ đọc đến hết
# print(fread.read(15), "\n") # đọc 15 ký tự đầu

# #Name_file_object.tell() vị trí con trỏ trong file hiện tại ở đâu
# print(fread.tell(), "\n")## vị trí thứ 20 --> trả về vị trí của fill pointer do là ký tự tiếng việt
# print(fread.read(), "\n")## đọc từ vị trí hiện tại đến hết




# #### "rb" chỉ được đọc thôi ko đc ghi và đọc dưới dạng nhị phân binary
# fread = open("I_O_inPy/Eg.txt", "rb")# chế độ "rb" ko hỗ trợ encoding= "utf-8"
# print(fread.read(), "\n")

# hom nay troi nang dep
# kien tri ky luat
# tu ky
# tinh yeu 
# phan boi trung thanh
# hi vong
# tu tuong
# khon canh

# #### "rb" chỉ được đọc thôi ko đc ghi và đọc dưới dạng nhị phân binary
# fread = open("I_O_inPy/Eg.txt", "rb")# chế độ "rb" ko hỗ trợ encoding= "utf-8"
# # print(fread.read(), "\n") # đọc ko xuống dòng
# # print(fread.readline())# read có xuống dòng nhưng chỉ read 1 dòng

# print(fread.readlines())## trả về 1 list


#### "r+", "rb+" sẽ ghi đè, ko tạo mới
#### r+ (read & write) Name_file_object.write(str) ghi chuỗi string
#fread = open("I_O_inPy/Eg.txt", "r+", encoding= "utf-8") ##encoding= "utf-8" cần dùng khi nếu trg file có ký tự tiếng việt sẽ ko đọc đc, và sẽ cần mã hóa về dạng tiếng việt để đọc ra thành công

#fread.write("Hôm qua trời mưa to tầm tã")#ghi vào đầu file nếu write trc khi read và đè lên số ký tự ghi vd ghi vào 25 ký tự sẽ đè lên 25 ký tự ở đầu văn bản

#nếu read trước write thì sẽ ghi vào cuối file
#print(fread.read(), "\n")
#fread.write("Hôm qua trời mưa to tầm tã")

##==>> chế độ r++ sẽ có 2 chế độ là ghi tiếp or ghi đè trừ trường hợp file ko tồn tại 
# fread = open("I_O_inPy/Eg1.txt", "r+", encoding= "utf-8")
# fread.write("Hôm qua trời mưa to tầm tã") ## file ko tồn tại sẽ báo lỗi ko có file

#### "r+", "rb+" sẽ ghi đè, ko tạo mới
#### "rb++" (read, write, binary)

### w(write only) chỉ cho phép ghi ko đc phép đọc
##"w" xóa sạch, ghi lại. file ko tồn tại -->> có tạo file mới



# hôm nay trời nắng đẹp
# kiên trì kỷ luật
# tự kỷ
# tình yêu 
# phản bội trung thành
# hi vọng
# tư tưởng
# khốn cảnh


##"w" xóa sạch, ghi lại. file ko tồn tại -->> có tạo file mới
# fread = open("I_O_inPy/Eg.txt", "w", encoding= "utf-8")
# fread.write("quy tac") ## xóa sạch dữ liệu cũ, ghi lại dữ liệu mới

# fread = open("I_O_inPy/Eg2.txt", "w", encoding= "utf-8")
# fread.write("quy tac") ## file Eg2 ko tồn tại -->> có tạo file mới

# ##"wb"(write only, binary) xóa sạch, ghi lại. file ko tồn tại -->> có tạo file mới
# fread = open("I_O_inPy/Eg.txt", "wb")
# fread.write(b'quy tac\r') ## xóa sạch, ghi lại dạng binary

# fread = open("I_O_inPy/Eg2.txt", "wb")
# fread.write(b'quy tac\r') ## xóa sạch, ghi lại dạng binary


#### w+ (read & write) # "w+"  
# fread = open("I_O_inPy/Eg.txt", "w+", encoding= "utf-8") ##  xóa sạch, đọc, ghi lại. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##  xóa sạch, ghi lại. file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file


# fread = open("I_O_inPy/Eg2.txt", "w+", encoding= "utf-8") ##  xóa sạch, đọc, ghi lại. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file

#### wb+ (read, write, binary) # "wb+"

# fread = open("I_O_inPy/Eg.txt", "wb+")##  xóa sạch, ghi lại dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file


# fread = open("I_O_inPy/Eg2.txt", "wb+")##  xóa sạch, ghi lại dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file

##### a (write only) ## ghi tiếp. file ko tồn tại -->> có tạo file mới

# fread = open("I_O_inPy/Eg.txt", "a", encoding= "utf-8")##   ghi tiếp. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##

# fread = open("I_O_inPy/Eg2.txt", "a", encoding= "utf-8")##   ghi tiếp. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##file ko tồn tại -->> có tạo file mới



##### a+ (read, write) ## đọc, ghi tiếp. file ko tồn tại -->> có tạo file mới

# fread = open("I_O_inPy/Eg.txt", "a+", encoding= "utf-8")##   ghi tiếp, đọc. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file


# fread = open("I_O_inPy/Eg2.txt", "a+", encoding= "utf-8")##   ghi tiếp,đọc. file ko tồn tại -->> có tạo file mới
# fread.write("quy tac") ##file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file

##### ab (write only, binary)## ghi tiếp dạng binary. file ko tồn tại -->> có tạo file mới
# fread = open("I_O_inPy/Eg.txt", "ab")##   ghi tiếp dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##


# fread = open("I_O_inPy/Eg2.txt", "ab")##   ghi tiếp dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##


##### ab+ (read, write, binary)## đọc, ghi tiếp dạng binary. file ko tồn tại -->> có tạo file mới

# fread = open("I_O_inPy/Eg.txt", "ab+")##   ghi tiếp, đọc dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file

# fread = open("I_O_inPy/Eg2.txt", "ab+")##   ghi tiếp, đọc dạng binary. file ko tồn tại -->> có tạo file mới
# fread.write(b'quy tac\r') ##
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file




#################---------- kiểm tra 1 số thuộc tính và phương thức của đối tượng file

#fread.closed ==> true nếu file đã đc đóng 


# fread = open("I_O_inPy/Eg.txt", "a+", encoding= "utf-8")##   ghi tiếp, đọc. file ko tồn tại -->> có tạo file mới
# fread.seek(0) #quay lại vị trí số 0 trg file
# print(fread.read()) ## dọc file

# fread.close()
# print(fread.closed) ##trả về true vì đã đóng file, nếu trả về false thì là file chưa đóng


# ## fread.mode ==>> access mode
# fread = open("I_O_inPy/Eg.txt", "a+", encoding= "utf-8")##   ghi tiếp, đọc. file ko tồn tại -->> có tạo file mới
# print(fread.mode) ##trả về a+ là chế độ đang mở file

# ## fread.name ==>> name file
# fread = open("I_O_inPy/Eg.txt", "a+", encoding= "utf-8")##   ghi tiếp, đọc. file ko tồn tại -->> có tạo file mới
# print(fread.name) ## tên file



#########-----------đặt lại tên


