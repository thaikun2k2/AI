#kiểu dữ liệu Dictionary là một kiểu dữ liệu có thể lưu trữ nhiều giá trị khác nhau, được định nghĩa bằng cặp key-value (khóa-giá trị). Mỗi key phải là duy nhất trong dictionary và được sử dụng để truy cập giá trị tương ứng.
#kết hợp ưu điểm giữa list và set, dictionary cho phép lưu trữ dữ liệu theo cặp key-value, trong đó key là một chuỗi hoặc một số, và value có thể là bất kỳ kiểu dữ liệu nào, bao gồm cả list hoặc dictionary khác.
# tập hợp không có thứ tự, có thể thay đổi, và cho phép trùng lặp. Dictionary được sử dụng rộng rãi trong Python để lưu trữ và quản lý dữ liệu phức tạp, như thông tin người dùng, cấu hình, hoặc kết quả của các phép tính.
#dictionary có chỉ số cho mỗi giá trị.


#list = ["đào", "hồng", "bưởi", "đào"]
########   0      1       2        3
#set = {"đào", "hồng", "bưởi"}


#dictionary = [0: "đào", 1: "hồng", 2: "bưởi", 3: "đào"]
#dictionary = [ 2: "bưởi",0: "đào", 1: "hồng", 3: "đào"]
###########    key: value
##==>>>>> x = {key1:value1, key2:value2, key3:value3,...} ===> kiểu dictionary
### 1 value có thể có nhiểu key khác nhau nhưng 1 key chỉ có thể có 1 value duy nhất



#####-----Practice-----#####
#Cách tạo một dictionary:
# dict = {0: "đào", 1: "hồng", 2: "bưởi", 3: "đào"}
# print(f'dict = {dict}')
# print(f'kiểu dữ liệu của dict == {type(dict)}')

# a = dict[1]
# print(f'a = {a}')

## set(mutable) + list(mutable) ==>> dict
#trường hợp 1: Dict mutable ko thứ tự, dấu {}, phtử: immutable, ko trùng lặp
#==>>>>> dict = {key1:value1, key2:value2, key3:value3,..., keyn:valuen} ===> kiểu dictionary
##dict : mutable

###-----key: -----###
# immutable -->> list,set,dict ko thể dùng làm key
# --> int, float, str, tuple.. có thể dùng làm key

###-----value: -----###
# immutable và mutable  ===>> ALL kiểu dữ liệu
# cho phép trùng lặp



#eg:
# #set: {}, dict: {}
# a = {}
# print(type(a))

# b = set() #phải khai báo thế này vì set và dict có cùng kiểu {}
# print(type(b))




#c = {"Ho va ten":"Nguyễn Văn Tón", "Ngay Sinh": "10 - 04 -2002", "so dt": 386188386}
#c = {1:"Nguyễn Văn Tón", 2: "10 - 04 -2002", 3: 386188386}
# c = {(1, 2, 3):"Nguyễn Văn Tón", 2: "10 - 04 -2002", "so dt": 386188386}
# ### ko thể để key == list[], set{}, dict{} vì là mutable: unhashable
# ### có thể để là kiểu tuple()
# ###Key ko đc trùng lặp nhau nếu ko sẽ bỏ đi các phần tử trùng lặp từ trái qua phải chỉ giữ lại 1 phần tử cuối cùng bên phải 

# print(f'c == {c}')
# print(f'type == {type(c)}')





### so sánh các phương thức của list anđ dict

