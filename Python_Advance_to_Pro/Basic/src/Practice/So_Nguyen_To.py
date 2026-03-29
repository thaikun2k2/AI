n = int(input("Nhập số: "))

def check_nguyen_to(n):
    if n < 2:
        print("Không phải là số nguyên tố")
    elif n == 2:
        print(f'{n} là số nguyên tố')
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f'{n} không phải là số nguyên tố')
                break
        else:
            print(f'{n} là số nguyên tố')

check_nguyen_to(n)