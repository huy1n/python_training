'''
for
while
vòng lặp lồng nhau
break: thoat vong lap
countinue: bỏ qua các câu lệnh bên dưới nó và chuyển sang một vòng lặp mới
'''

# for _ in range(5):
#     print('hello world')

# for i in range(21):
#     if i % 2 == 0:
#         print(i, end=' ')

# s = input('> ')
# while s != 'q':
#     print('hello')

# vòng lặp for lặp số lần lặp xác định, while lặp số lần không xác định

for i in range(5):
    for j in range(3):
        print(i, j, sep=' - ')

for i in range(1, 21):
    if i % 2 == 0:
         continue #bỏ qua fong print
    print(i, end = ' ')