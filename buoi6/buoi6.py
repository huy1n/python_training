'''
if - elif - else
'''
# Cú pháp:
# if điều_kiện:
    # câu_lệnh
""" thoi_tiet = 'nang'
if thoi_tiet == 'nang':
    print('oke')
else:
    print('noo')

num = int(input('nhap n: '))

if num >0:
    print('so duong')
elif num == 0:
    print('so 0')
else:
    print('so am')

print('n chia het cho 2' if num % 2 == 0 else 'nn khong chia het cho 2') """

# hàm nhập nâng cao
# khi nhập bằng input() giá trị sẽ là 1 chuỗi, hàm split() sẽ tách chuỗi ra thành các phần tử (mặc định không)
# truyền tham số sẽ cắt theo " ", sau đó hàm map() sẽ convert chuỗi thành int
""" s = 'a b c'
print(s.split())
list1 = input().split()
print(list1)
print(list(map(int, list1))) """

# nhập nhiều dãy số trên cũng 1 hàng
""" a, b = map(int, input().split())
print(a if a <b else b) """

# hàm eval() dùng để đánh giá biểu thức bên trong chuỗi
""" print(eval('1+2'))
lst = list(map(eval, input().split()))
print(lst) """

# in ra trên cùng 1 hàng cách ra bởi dấu cách
""" lst = [1, 2, 3, 4]
print(*lst, sep = "%") """

# format
x = 2.4567
print(format(x, '.2f'))

# hàm round(): làm tròn
# hàm pow() tính lũy thừa
# hàm sorted() dùng để sắp xếp và trả về 1 list mới
# ord() trả về mã ascii
# divmod() phép chia trả về số nguyên và số dư




































