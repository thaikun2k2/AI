### số = tổng ước trừ chính no
#eg: 6 = 1 + 2 + 3

def perfect__number(n):
    sum = 0
    if (n < 2):
        print("Không phải là số hoàn hảo")
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    if (sum != n):
        print("Không phải là số hoàn hảo")
    else:
        print("Là số hoàn hảo")
        
n = int(input("Nhập số: "))
perfect__number(n)
