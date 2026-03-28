""" list  Comprehension"""
###ngoại lệ có thể viết gộp trg python

list1 = [1, 2, 3, 4, 5]
list_Comprehension = [x**2 for x in list1]
print(f'{list_Comprehension}')

list_Comprehension2 = [x for x in list1 if x %2 == 1]
print(list_Comprehension2)

list_Comprehension3 = [x if x %2 == 0 else x + 2 for x in list1]
print(list_Comprehension3)

""" Dictionary  Comprehension"""
#[k:v for item in iterable]
dict = {k: k**2 for k in list1}
print(dict)



""" Set  Comprehension"""
#{item for item in iterable}

m_string = "Minhmin"
sets = { letter for letter in m_string}
print(sets)

""" Multiple loops """

new_list = [[i for i in range(5)] for _ in range(5)]
print(new_list)

srr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]
new_srr = []

for row in srr:
    for num in row:
        new_srr.append(num)
print(new_srr)
