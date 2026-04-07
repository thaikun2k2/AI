"""
🎯 1. Mục đích chính của Big-O (rút gọn từ bài giảng)

👉 Big-O dùng để:

Đo và so sánh độ hiệu quả của thuật toán khi dữ liệu tăng lên

🎯 Time Complexity là gì?

Time Complexity (độ phức tạp thời gian) là cách đo số lượng phép toán mà thuật toán cần thực hiện khi kích thước input tăng lên.

🧠 Hiểu đơn giản

👉 Không đo thời gian thực (giây) ❌
👉 Mà đo:

Thuật toán chạy bao nhiêu bước khi dữ liệu lớn dần


Time complexity: O(wh) # w trong lượng, h chiều cao

Types of Runtimes:
O(N), O(N**2), O(2**N)

Độ phức tạp tăng theo thời gian và độ lớn của đầu vào:









"""



## độ phức tạp O(n)
# def print_items(n):
#     for i in range(n):
#         print(i)
        
# # DO NOT CHANGE THIS LINE:
# print_items(10)

## độ phức tạp O(n + n) = O(2n)
# def print_items(n):
#     for i in range(n):
#         print(i)
    
#     for j in range(n):
#         print(j)
# # DO NOT CHANGE THIS LINE:
# print_items(10)


### vòng lặp lồng nhau dộ phức tạp 2 for = n*n=n**2
## độ phức tạp O(n**2)
# def print_items(n):
#     for i in range(n):    #--------->O(n)
#         for j in range(n):   #------>O(n)
#             print(i,j)    #---------> n*n == n**2
# # DO NOT CHANGE THIS LINE:
# print_items(10)


# ## độ phức tạp O(n**3)
# def print_items(n):
#     for i in range(n):    
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)
# # DO NOT CHANGE THIS LINE:
# print_items(10)


# ## độ phức tạp O(n**2 + n)
# def print_items(n):
#     for i in range(n):    
#         for j in range(n):
#             print(i,j)
#     for k in range(n):
#         print(k)
# # DO NOT CHANGE THIS LINE:
# print_items(10)


### đọ phức tạp time O(log n)
##input vào siêu lớn 


# ###space complexity(độ phức tạp không gian)

# #Eg:
# # chiếm dụng bộ nhớ và ngăn xếp
# def sum(n):
#     if n <= 0:
#         return 0
#     return n + sum(n - 1)
# ## hàm đệ quy này sẽ thực hiện xếp vào ngăn xếp không gian gây chiếm dụng bộ nhớ thực tế 
# #Eg nếu chuyền vào n = 3 thì sẽ 3 ngăn xếp. khi n= 0 thì kết thúc.
# sum(3)


## trường hợp n cko chiếm dụng độ phúc tạp O(n)

# def pair_sum_sequence(n):
#     total = 0
#     for i in range(n):
#         total = total + pair_sum(i, i + 1)
#     return total


# def pair_sum(a, b):
#     return a + b

# x1 = pair_sum_sequence(8)
# print(x1)
# x = pair_sum(1, 2)
# print(x)






############


###---different term for input - add vs multiply


# ##Add the Runtime: O(a + b)
# # độ phức tạp O(n + n) = O(2n)
# def print_items(a,b):
#     for i in range(a):
#         print(i)
    
#     for j in range(b):
#         print(j)
# # DO NOT CHANGE THIS LINE:
# print_items(10, 5)




# #Multiply the Runtimes: O(A * B)
# def print_items(a,b):
#     for i in range(a):
#         for j in range(b):
#             print(i, j)

# print_items(10, 5)






