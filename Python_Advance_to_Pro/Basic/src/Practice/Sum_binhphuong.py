n = int(input("Nhập n: "))
# def Sum_binhphuong(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i**2
#     return sum

def Sum_binhphuong(n):
    return n * (n + 1) * (2 * n + 1) // 6


print("Tổng bình phương của n là: ", Sum_binhphuong(n))