'''
câu điều kiện if - elif - else
vòng lặp for
vòng lặp while
pass, break
'''

""" weather = input('nhap thoi tiet')

if weather != 'nang':
    print('mua')
else:
    print('lam ram') """

""" point = int(input('nhap 1 point: '))

if point is False:
    print('0')
else:
    print('1') """

""" dtb = float(input('nhap diem trung binh: '))

if dtb >= 8:
    print('gioi')
elif dtb >=6.5 and dtb < 8:
    print('kha')
else:
    print('ngu') """

""" for i in range(1, 21):
    if i % 2 != 0: # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        print(i)
    else:
        print(f'{i} \t')
 """

""" lst = ['banana', 'dragonfruit', 'coconut', 'melon', 'apple']

str = 'lequangtu'

for i in str:
    print(i, end = ' ') """

""" name = input('name: ')

while True:
    if name == 'nam':
        print('oke bro')
        break
    else:
        print('dang nguyen haong nam') """

""" n = int(input('nhap chieu cao'))

for i in range(n):
	for j in range(n):
		if j==0 or i == j or j==n-1:
			print('*', end = ' ')
		else:
			print(" ", end = ' ')
	print() """

# i là hàng, j là cột trong vòng lặp lồng nhau


""" n = int(input('nhap chieu cao'))

for i in range(n):
	for j in range(n):
		if j==0 or i == j or i==n-1:
			print('*', end = ' ')
		else:
			print(" ", end = ' ')
	print() """