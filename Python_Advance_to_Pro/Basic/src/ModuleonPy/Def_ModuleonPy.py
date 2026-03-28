
#hàm tính giai thừa
def giaithua(n):
    if n == 1:
        return 1
    else:
        return n*giaithua(n-1)

#hàm tính tổng 2 số a, b
def sum2numbers(a, b):
    t =a + b
    return t
