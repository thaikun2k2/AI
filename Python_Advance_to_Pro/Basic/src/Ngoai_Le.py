## Exception(Ngoại lệ)

###==> xảy ra 1 ngoại lệ (điều ko mong muốn) đây là 1 lỗi ==>> tiến trình bị tạm dừng ==>> để xử lý ngoại lệ

## Trg python: 1 ngoại lệ là 1 đối tượng, đại diện cho 1 lỗi
##Bình thường: run program ==>> xảy ra 1 lỗi ==>> báo lỗi ==>> kết thúc program

## nếu dùng ngoại lệ: run program ==>> xảy ra 1 lỗi ==>> dừng program ==>> xủ lý lỗi ==>> chạy tiếp program
# try: 
#     fread = open("I_O_inPy/Eg2.txt", "r", encoding= "utf-8") ##encoding= "utf-8" cần dùng khi nếu trg file có ký tự tiếng việt sẽ ko đọc đc, và sẽ cần mã hóa về dạng tiếng việt để đọc ra thành công
#     #fread = open("I_O_inPy/Eg.txt", "r", encoding= "utf-8")
# except IOError:
#     print("có lỗi mở file")
# else:
#     print(fread)
#     print(fread.read(), "\n") ## read tất cả file



# try: 
#     fread = open("I_O_inPy/Eg2.txt", "r", encoding= "utf-8") ##encoding= "utf-8" cần dùng khi nếu trg file có ký tự tiếng việt sẽ ko đọc đc, và sẽ cần mã hóa về dạng tiếng việt để đọc ra thành công
# except IOError:
#     fread = open("I_O_inPy/Eg.txt", "r", encoding= "utf-8")
#     print(fread)
#     print(fread.read(), "\n") ## read tất cả file
# else:
#     pass###pass là bỏ qua vì đã thành công


##--==>> nếu có nhiều loại lỗi khác nhau ==>> có nhiều ngoại lệ
##--==>> ngoại lệ: đưa ra phương án xử lý lỗi ==>> tốn time, code dài, tiêu tốn nhiều bộ nhớ 

##-===có cách nào không???>>>>>> để kết hợp ưu điểm của ngoại lệ và ko ngoại lệ =>>> giải pháp đưa ra là viết code sao cho ko có lỗi xảy ra, đoạn code nào có nguy cơ sảy ra lỗi


###########################################################################################################################

####-----Cú pháp để use ngoại lệ: 
"""
try:
    khối lệnh nghi ngờ có lỗi
except lỗi 1:
    Phương pháp xử lý lỗi 1
except lỗi 2:
    Phương pháp xử lý lỗi 2
except lỗi 3:
    Phương pháp xử lý lỗi 3
else:
    không có lỗi thì làm như thế này!

    
khối lệnh chắc chắn ko có lỗi


các built in exception:
IOError => open(file) FileNotFound
ZeroDivisionError: lỗi không chia được cho 0

ValueError: lỗi về mặt giá trị

ImportError: lỗi import cái ko xác định

IndexError: lỗi không có giá trị

TypeError: lỗi kiểu dữ liệu
"""

# ##eg:
###ZeroDivisionError: lỗi không chia được cho 0
# try: 
#     a = 36
#     b = 0
#     x = a/b
# except ZeroDivisionError:
#     print("xảy ra lỗi không chia được cho 0\n")

# print("Python")


###ValueError: lỗi về mặt giá trị
# try: 
#     a = 36
#     b = int("a")
#     x = a/b
# except ValueError:
#     print("xảy ra lỗi value giữa kiểu dữ liệu của các biến\n")


###ImportError: lỗi import cái ko xác định
# try:
#     from math import abcd
# except ImportError:
#     print("lỗi import không xác định")



###IndexError: lỗi không có giá trị
# try: 
#     a = ["1"]
#     e = a[3]
# except IndexError:
#     print(" lỗi không có giá trị")


##eg:
# try: 
#     from math import abcd
#     a = 36
#     b = 0
#     x = a/b
#     c = 36
#     d = int("a")
#     y = c/d
#     j = ["a"]
#     e = j[3]
# except ZeroDivisionError:
#     print("xảy ra lỗi không chia được cho 0\n")
# except ValueError:
#     print("xảy ra lỗi value giữa kiểu dữ liệu của các biến\n")
# except ImportError:
#     print("lỗi import không xác định")
# except IndexError:
#     print(" lỗi không có giá trị")

# print("Python")

###TypeError: lỗi kiểu dữ liệu
# try:
#     a = 36
#     e = a[12]
# except TypeError:
#     print("lỗi kiểu dữ liệu")