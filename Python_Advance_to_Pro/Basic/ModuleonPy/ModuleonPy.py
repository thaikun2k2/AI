#Mục đích: Tổ chức code easy understand and dễ sử dụng hơn
# Module is: 1 file python đuôi .py
# ĐK: def,class, có sẵn or do user viết 
#User def on Module:
#C1: import Name_module                    | ==>Use: gọi hàm: Name_module.Name__def()
#C2: from Name_module import Name_def      | Use: Name_def ==>> gọi hàm: Name__def()
#C3: from Name_module import*              | ==>>> Use: ko gọi đc_NameDef
#File module cùng cấp vs file chính (cùng 1 folder)


#Trường hợp khác cấp vs file chính (khác 1 folder) ->> add đường dẫn file module vào system





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

from Def_ModuleonPy import*
x = giaithua(3)
y = sum2numbers(3, 5)

print(x)
print(y)