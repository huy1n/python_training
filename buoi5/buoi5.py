'''
- advanced set
- dictionary
- sum, len, min, max, join
'''

set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 3, 9, 10}
set_3 = set_1.intersection(set_2)  # tim phan tu chung cua 2 set, set được trả về là 1 set mới
print(set_1 & set_2) # như trên
# chỉ sử dụng được cả 2 phần tử đều là set
print(set_3)

set4 = set_1.difference(set_2) # tìm phần tử khác nhau (có trong set1 nhưng không nằm trong set2)
print(set_1 - set_2)
print(set4)

set5 = set_1.union(set_2) # lấy ra tất cả các phần tử trong cả 2 set
print(set_1 | set_2)
print(set5)

set6 = set_1.symmetric_difference(set_2) # lấy tất cả nhưng trừ đi phần chung của cả 2 set
print(set_1 ^ set_2)
print(set6)

'''
dictionary: key:value
'''
import json

dict = {
    'name': 'bob',
    'age': 23,
    'gender': 'male' 
    # các phần tử trong dict phải là set (nghĩa là các key không được trùng nhau)
}
print(json.dumps(dict, indent=4))

value = dict['age'] # lấy ra value của key age
value1 = dict.get('id', 'sv001') # lấy ra value của key age, nếu không có key thì sẽ trả về giá trị None, ngoài ra còn có thể chỉ định value của nó

print(value)
print(value1)

dict['id'] = 'sv001' # tạo thêm key và value
dict['age'] = '43' # nếu tạo key mới có tên trùng với key cũ thì nó sẽ update 
print(dict)

dict.update(classes = 'dth') # thêm cặp key và value mới vào dict, có thể thêm nhiều
print(json.dumps(dict, indent=4))

'''info = {
    'grade': [10, 8, 10]
    # tạo 1 dict phụ dùng nó để thêm vào dict sẵn có
}'''

info = [
    ('grade', [10, 8, 10])
    # tạo 1 list tuple dùng nó để thêm vào dict sẵn có
]

dict.update(info)
print(json.dumps(dict, indent=4))

dict.pop('grade') # xóa cặp key value
del dict['id'] # cách 2

tup = dict.popitem() # xóa đi phần tử cuối cùng trong dict và trả về kết quả là 1 tuple
print(tup)
print(dict)

# lấy ra key và tạo thành 1 list
keys = list(dict)
print(keys)
# lấy ra value và tạo thành 1 list
value = list(dict.values())
print(value)
# lấy ra key và values và tạo thành 1 list
items = list(dict.items())
print(items)

list = [1, 2, 3, 4, 5]
total = sum(list) # tinh tong cac phan tu co torng list
print(total)

# ví dụ nâng cao
list1 = [[1, 2, 3, 4, 5, 6], [10, 11, 12, 13]]
total1 = sum(list1, [0]) # có tác dụng giống như extend hay append
print(total1)

lst = [4,3,2,1]
s = '-'.join(map(str, lst)) # hàm map dùng để convert 1 list số thành 1 list string '-' là ngăn cách bởi dấu - 
# joint chỉ áp dụng cho các list chỉ chứa phần tử là chuỗi
print(s)

def double(x):
    return x * 2 

print(set(map(double, [1, 2, 3 ,4])))