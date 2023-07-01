# set nâng cao

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 4, 7, 9, 16}

# tìm phần tử chung của 2 set
set3 = set1.intersection(set2)
print(set1 & set2)
print(set3)

# tìm phần tử khác nhau, có trong set 1 nhưng không có trong set 2
set4 = set1.difference(set2)
print(set1 - set2)
print(set4)

# lấy ra phần tử có trong 2 set
set5 = set1.union(set2)
print(set1 | set2)
print(set5)

# lấy tất cả nhưng trừ đi phần chung
set6 = set1.symmetric_difference(set2)
print(set1 ^ set2)
print(set6)
