n = int(input("Nhập vào số nguyên dương n = : "))

l = []
def Fibonacci_N(n):
    global l
    if n <= 2:
        return l
    else:
        return Fibonacci_N(n-1) + Fibonacci_N(n-2), l

    
Fibonacci_N(n)
print(l)