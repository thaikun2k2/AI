#Mục đích: Tổ chức code easy understand and dễ sử dụng hơn
# Module is: 1 file python đuôi .py
# ĐK: def,class, có sẵn or do user viết 
#User def on Module:
#C1: import Name_module                    | ==>Use: gọi hàm: Name_module.Name__def()
#C2: from Name_module import Name_def      | Use: Name_def ==>> gọi hàm: Name__def()
#C3: from Name_module import*              | ==>>> Use: ko gọi đc_NameDef
#File module cùng cấp vs file chính (cùng 1 folder)


#Trường hợp khác cấp vs file chính (khác 1 folder) ->> add đường dẫn file module vào system
#but py chỉ import đc các file cùng cấp or các file hệ thống




#########--------C1:import Name_module
#eg
# import Def_ModuleonPy
# x = Def_ModuleonPy.giaithua(3)
# y = Def_ModuleonPy.sum2numbers(3, 5)
# print(x)
# print(y)

#change name ngắn hơn nữa
# import Def_ModuleonPy as mo
# x = mo.giaithua(3)
# y = mo.sum2numbers(3, 5)

# print(x)
# print(y)

#########--------C1:import Name_module

#########--------C2:from Name_module import Name_def
# from Def_ModuleonPy import giaithua
# from Def_ModuleonPy import sum2numbers
# x = giaithua(3)
# y = sum2numbers(3, 5)

# print(x)
# print(y)
#########--------C2:from Name_module import Name_def


#########--------C3: from Name_module import*

# from Def_ModuleonPy import*
# x = giaithua(3)
# y = sum2numbers(3, 5)

# print(x)
# print(y)

#########--------C3: from Name_module import*









#Eg: difficult folder 

# import os 
# path_module = os.path.abspath(os.path.join("Module")) #thêm đường dẫn đến thư mục
# print(path_module) ## in đường dẫn đến thư mục

# import os ,sys
# path_module = os.path.abspath(os.path.join("Module")) #thêm đường dẫn đến thư mục
# print(path_module, "\n") ## in đường dẫn đến thư mục
# sys.path.append(path_module)
# s = sys.path
# for i in s:
#     print(i)


# #Ví dụ: Thư mục khó (khác cấp)
# # Import các module cần thiết để xử lý đường dẫn
# import os ,sys
# # Tạo đường dẫn tuyệt đối đến thư mục "Module"
# script_dir = os.path.dirname(__file__)
# path_module = os.path.join(script_dir, "Module")
# # In đường dẫn để kiểm tra
# print(path_module, "\n") ## in đường dẫn đến thư mục
# # Thêm đường dẫn vào sys.path để Python có thể import module từ đó
# sys.path.append(path_module)
# # Import các hàm từ module Def_module trong thư mục Module
# from Def_module import giaithua, sum2numbers
# # Gọi hàm giaithua với tham số 3
# x = giaithua(3)
# # Gọi hàm sum2numbers với tham số 3 và 5
# y = sum2numbers(3, 5)

# print(x)
# print(y)
