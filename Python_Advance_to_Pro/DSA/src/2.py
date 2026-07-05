def add_two_numbers(l1, l2):
    resuft = []
    num1 = 0
    for x1 in l1:
        num1 = num1 * 10 + x1
    num2 = 0
    for x2 in rangel2:
        num2 = num2 * 10 + x2
    sum = num1 + num2
    reverse_num = int(str(sum)[::-1])
    while reverse_num > 0:
        resuft.append(reverse_num % 10)
        reverse_num //= 10

    resuft.reverse()
    return resuft        

l1 = [2, 4, 3]
l2 = [5, 6, 4]
res = add_two_numbers(l1, l2)
print(res)