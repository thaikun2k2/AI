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

##-===>>>>>> để kết hợp ưu điểm của ngoại lệ và ko ngoại lệ





