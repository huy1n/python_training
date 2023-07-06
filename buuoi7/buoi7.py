""" 
list, set, tuple, dict comprehensions
zip, enumerate
"""

""" lst = [1, 2, 3, 4]
_tuple = ("trai chuoi", "tao", 'dua hau', 'cu', 'qqq')
_dict = {
    'name': 'nam',
    'age': 21
}
_set = {1, 2, 3, 4, 5}

_zip = zip(lst, _tuple)
print(tuple(_zip)) """

# _tuple = ("trai chuoi", "tao", 'dua hau', 'cu', 'qqq')
# print(list(enumerate(_tuple)))

""" list comprehensions """
import json
lst = [1, 2, 3, 4]  # 2 4 6 8

new_lst = []
for i in lst:
    v = i*2
    new_lst.append(v)
print(new_lst)

# compre
# 1. tao 1 iterable trong
# 2. dinh nghia 1 bien bat ki
# 3. bieu thuc
new_lst1 = [a*2 for a in lst]
print(new_lst1)

# set compre
_set = {'b', 'u', 'c'}

new_set = set()
for c in _set:
    h = c.upper()
    new_set.add(h)
print(new_set)

new_set1 = {s.upper() for s in _set}
print(new_set1)

# dict compre
dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

# for key in dict:
#     dict[key] *= 2

print(json.dumps(dict, indent=4))

new_dict = {
    k: v*2 for k,v in dict.items()
}
print(json.dumps(new_dict, indent=4))

