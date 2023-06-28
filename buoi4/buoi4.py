'''
- set{} không chứa phần tử giống nhau
- tuple()
'''
# tuple
tup1 = 1, 2, 3
tup2 = (1, 2, 3)
print(type(tup1))
print(type(tup2))

tup1 = 1, 2, 3
print(tup1[0])
tup1 += (4, 1, 2, 5, 7)
print(tup1)

# set
set1 = set()
print(set1)
set1.add(1)
set1.add(1)
set1.add(1)
set1.add(1)
set1.add("kenny")
set1.update([2, 3, 4, 5])
# không thể chèn đc list vào set vì các giá trị list có thể được thay đổi
set1.add([2, 3, 4, 5])
set1.remove(1)
set2 = set1.copy()
print(set1 is set2)
print(set1 == set2)
print(set1)
set1.clear()
print(set1)

set1 = {1, 2, 34, 4, 65, 677}
any_value = set1.pop()
print(any_value)

'''

'''
