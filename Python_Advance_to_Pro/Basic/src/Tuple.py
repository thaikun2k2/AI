#######################################################################################################


###List là dùng []
###Tuple là dùng ()

# ls = ["a", 5, 4, 8]
# tp = ("a", 5, 4, 8, 5, 1, 4)
# tp1 = ("b", 6, 7, 9)
# strr = "abcde"


# print(ls)
# print(type(ls))

# print(tp)
# print(type(tp))
# print(id(tp))
# print("\n")

# x = tp[0]
# print(x)
# print(type(x))
# print("\n")
# print(id(x))

# x1 = tp + tp1
# print(x1)
# print(type(x1))
# print(id(x1))

# x2 = tp*3
# print(x2)
# print(type(x2))
# print(id(x2))

# z = tp[0:2]
# print(z)
# print(type(z))
# print("\n")

# x = 5 in tp
# print(x)

# for i in tp:
#     print(i)


##########Sự =! : immutable and mutable 
###immutable: không thể thay đổi được giá trị của nó sau khi đã được tạo ra eg như kiểu tuple()
###mutable: có thể thay đổi được giá trị của nó sau khi đã được tạo ra eg như kiểu list[]

####->> list thay đổi, còn tuple cố định : giá trị, thứ tự, kích thước (cùng ô nhớ (id) )
### tuple ko thể dùng remove, append, insert, pop, clear,... như list
### tuple có thể dùng count, index, len,... như list

# g = tuple(strr)
# print(g)

# e = tuple(tp)
# print(e)

# print(len(tp))
# print(tp.count(5)) ## số lần xuất hiện của 5 trong tp

# print(tp.index(4))## vị trí của 4 trong tp
# print(tp.index(5, 1, 6)) ## tìm vị trí của 5 trong tp từ vị trí 1 đến vị trí 6
# print("\n")
# #list, str, tuple cho phép trùng lặp
# i = 0
# x = 3
# y = 6

# if i in tp[x:y]:
#     x = tp.index(i, x, y) ###kiểm tra ko thấy sẽ báo lỗi, nên cần có vòng if để ktra
#     print(x)
# else:
#     print(f'ko có {i} trong tp từ vị trí {x} đến vị trí {y}')


# ###lưu ý: khi khai báo tuple có 1 phần tử thì phải có dấu phẩy sau phần tử đó để phân biệt với kiểu dữ liệu khác
# tp2 = (5,)
# print(tp2)
# print(type(tp2))

# tp3 = (5)
# print(tp3)
# print(type(tp3))


#######################################################################################################

# x = [2, 4, "a"]
# y = [2, 4, "a"]
# print(x == y) ## so sánh giá trị của x và y
# print(x is y) ## so sánh địa chỉ hay còn gọi là có trùng nhau hay ko của x và y, != ở ô nhớ 



## x is y  <=> id(x) == id(y) and x == y
### các kiểu dữ liệu mutable như list, dict, set, byteaarray,...
### các kiểu dữ liệu immutable như int, float, str, tuple,... 
### ở tuple a và b đều chỉ lưu ở cùng 1 ô nhớ nên a is b sẽ trả về True


# a = (2, 4, "a")
# b = (2, 4, "a")
# print(a == b) ## so sánh giá trị của a và b
# print(a is b) ## so sánh địa chỉ hay còn gọi là có trùng nhau
# print(id(a))
# print(id(b))
# print("\n")

# 2 phần tử ở 2 danh sách co kiểu khác nhau là mutable thì sẽ không cùng 1 ô nhớ nữa!

# c = (2, 4, [1, 3])
# d = (2, 4, [1, 3])
# print(c == d) ## so sánh giá trị của c và d
# print(c is d) ## so sánh địa chỉ hay còn gọi là có trùng nhau
# print(id(c))
# print(id(d))
# print("\n")


# c = (2, 4, [1, 3])
# d = (2, 4, [1, 3])
# print(c[0] == d[0]) ## so sánh giá trị của c và d
# print(c[0] is d[0]) ## so sánh địa chỉ hay còn gọi là có trùng nhau
# print(id(c[0]))
# print(id(d[0]))
# print("\n")


# h = (2, 4+5j, 9)
# g = (2, 4+5j, 9)
# print(h[1] == g[1]) 
# print(h[1] is g[1]) 
# print(id(g[1]))
# print(id(h[1]))
# print("\n")

# i = [2, 4, (5, 7)]
# o = [2, 4, (5, 7)]
# print(i[2] == o[2]) 
# print(i[2] is o[2]) ##a[2] == b[2] là immutable vì cùng trỏ đến 1 ô nhớ chứa tuple (5, 7) nên sẽ trả về True
# print(type(i))
# print(type(o))
# print("\n")



# u = [2, 4, {5, 7}]
# j = [2, 4, {5, 7}]
# print(u[2] == j[2]) 
# print(u[2] is j[2]) ##a[2] != b[2] là set là mutable nên sẽ trả về False vì 2 set {5, 7} ở 2 ô nhớ !=
# print(type(u))
# print(type(j))
# print("\n")

#############################################################################################


##hàm hash là một hàm băm, được sử dụng để tạo ra một giá trị duy nhất (hash value) cho một đối tượng.
##hash value được sử dụng để xác định vị trí của đối tượng trong một cấu trúc
## dữ liệu như bảng băm (hash table) hoặc để kiểm tra tính toàn vẹn của dữ liệu.
##hàm hash có thể được sử dụng để kiểm tra xem một đối tượng có thể được
##sử dụng làm khóa trong một cấu trúc dữ liệu như dictionary hay không. Nếu một đối tượng có thể được hash, nó có thể được sử dụng làm khóa trong một dictionary.

# x ="abc"
# z = hash(x)
# print(" kết quả sau hàm hash:  ",z) 

# y = "abcdeghretyghjklcgtvhbjknkyuihjkl"
# a = hash(y)
# print(" kết quả sau hàm hash:  ",a)#

# b = (2, 4, 1, 1, 0, "a")
# c = hash(b)
# print(" kết quả sau hàm hash:  ",c)

# d = range(200)
# e = hash(d)
# print(" kết quả sau hàm hash:  ",e)

# g = 4,556677
# h = hash(g)
# print(" kết quả sau hàm hash:  ",h)

# j = [2, 4, 1, 1, 0, "a"]
# k = hash(j) 
# print(" kết quả sau hàm hash:  ",k) ## sẽ báo lỗi vì list là mutable nên ko thể hash được   

# i = {2, 4, 1, 1, 0, "a"}
# l = hash(i)
# print(" kết quả sau hàm hash:  ",l) ## sẽ báo lỗi vì set là mutable nên ko thể hash được 

###=>> dữ liệu theo kiểu mutable sẽ không thể đưa vào hash vì nó là unhashable object

# o = (2, 4, (1, 3))
# p = hash(o) 
# print(" kết quả sau hàm hash:  ",p) 

# k = (2, 4, [1, 3])
# l = hash(k) 
# print(" kết quả sau hàm hash:  ",l) ## sẽ báo lỗi vì tuple chứa list là mutable nên ko thể hash được

###=>> dãy có độ dài bằng nhau



########################################################################################

############ so sánh các kiểu dữ liệu:

#######kiểu số (immutable)
#hashable
#toán tử toán học
#==, !=, >, <, >=, <=,is,is not,...
#int(), float(), complex(), bool()
#randrange()
#----------
#----------
#-----
#max(), min()
#------
# del x
#------
#------
#------
#------
#------
#------
#------
#------






#######kiểu String (immutable)
#hashable
#[n], [n:m], [n:m:k],+, in, for,... 
#==, !=, >, <, >=, <=, is, is not
#chr(), ord(), str(), repr()...
#choice(), count()
#index()
# find()
#len()
#max(), min()
#replace(old,new)
# del x
#------
#------
#------
#------
#------
#------
#z = x[::--1]
#------




#######kiểu Tuple (immutable)
#hashable
# if nếu có 1 ptu con là mutable thì hàm này sẽ là mutable
#[n], [n:m], [n:m:k], +, in, for,... 
#==, !=, >, <, >=, <=, is, is not, ...
#tuple()
#choice(), count()
#index()
#------
#len()
#max(), min()
#------
#del x
#------
#------
#------
#------
#------
#------
#------
#------




#######kiểu List (mutable)
#unhashable
#[n], [n:m], [n:m:k], +, in, for,...
#==, !=, >, <, >=, <=, is, is not,...
#list()
#choice(), count()
#index()
#------
#len()
#max(), min()
#tenlist[n]  new
#del x
#clear()
#remove()
#del x[n]
#append(), sort()
#x.extend(y)
#insert(index, ob)
#pop()
#reverse()
#------
#copy()
