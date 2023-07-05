""" 
list, set, tuple, dict comprehensions
"""
lst = [1, 2, 3, 4]
new_lst = [v*2 for v in lst]
print(new_lst)

set_a = {'a', 'b', 'c'}
set_b = {i.upper() for i in set_a}
print(set_b)

dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
new_dict = {
    k: v * 2
    for k, v in dict.items()
}

print(new_dict)

""" zip. enumerate """

lst = [1, 2, 3, 4]
tup = (1, 2, 3, 4)
_zip = zip(lst, tup)
print(list(_zip))

lst1 = ['a', 'b', 'c']
print(list(enumerate(lst1)))

stu = {
    'name': 'bob',
    'age': 23,
    'id': 'sv001'
}

for item in enumerate(lst):
    idx, value = item
    print(f'{idx} - {value}')
