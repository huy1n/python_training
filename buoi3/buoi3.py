numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)
index = numbers.index(3)
print(index)
amount = numbers.count(3)
print(amount)
amount = numbers.count(1000)
print(amount)
numbers.clear()
print(numbers)

amount = len(numbers)
print(amount)

numbers.insert(0, 1000)  # đối số đầu tiên là vị trí
print(numbers)
number.append(5)  # append truyển tham số vào đuôi
print(number)

number.remove(2)
print(number)

last_value = number.pop()
print(last_value)
print(number)

number.extend([1, 2, 3, 45])
print(number)

max_values = max(numbers)
min_values = min(numbers)
print(max_values)
print(min_values)
'''
list in list
copy list
list slicing

'''

friend = [['john', 23], ['nami', 24], ['cow', 25]]
print(friend[0][1])

lst1 = [1, 2, 3]
lst2 = lst1

if lst1 is lst2:
    print('true')

lst3 = [4, 5, 6]
lst4 = lst3.copy()
print(lst3 is lst4)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:3])  # nó sẽ đếm tới bị trí thứ 3 nhưng không lấy nó
