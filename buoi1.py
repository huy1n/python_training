print("hello  world")
"""
    day la comment cho dong hello world!
"""

# Ctrl + /: comment
# copy nhanh: shift + alt + arrow down
# copy: cuoi dong roi ctrl + c
# muốn sửa nội dung giống nhau: ctrl + D
# muốn comment 1 đoạn văn bản dài """ """

# các kiểu dữ liệu cơ bản: int, float, string, complex, boolean
# type(): kiểm tra kiểu dữ liệu của biến
s = 4
print("s thuoc kieu du lieu: ", type(s))

x = 4.1
print(type(x))

str = "hello"
print("str thuoc kieu du lieu: ", type(str))

complex = 5 + 4j
print(" thuoc kieu du lieu: ", type(complex))
print(complex.imag)
print(complex.real)

bool1 = True
bool2 = False
print(type(bool1))

# toán tử: +, -, *, /, //, %, **
x = 5
y = 6
print(x + y)
print(x - y)
print(x // y)
print(11 // 2)
print(11 % 2)
#  11 chia 2 được 5 dư 1

# chia lấy phần nguyên (//) lấy phần không dư: 5
# chia lấy phần dư (%) lấy phần dư: 1

# =, ==, +=, -=, /=, //=, %=, **=
x = 5
x = x + 5
print(x)
print("-"*30)
x = 5
x += 5
print(x)

x = 9
x -= 6
print(x)

# toán tử so sánh: ==, >, <, >=, <=, != (khác)
# toán tử so sánh nó trả về 1 giá trị là True hoặc là False
x = 5
y = 7
print(x > y)
print(x < y)

# and, or, not
# and: biểu thức đúng nếu cả 2 toán hạng đều đúng, nếu có 1 toán hạng sai thì sai
print( 5 == 5 and 4 == 4)
print( 5 == 5 and 4 != 4)

# or: chỉ cần 1 thằng true thì kết quả trả về là True, tất cả điều kiện False thì kết quả trả về là False
print(5 == 5 or 4 == 3)

#not
print(not 5 == 5)

print(True and True)
print(True and False)
print(False and False)
print(False and True)
print("-"*30)
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print("-"*30)
print(not True)
print(not False)
print("-"*30)
print(bool(0))
print(bool(1))
print(1 and 2)
print("-"*30)

# các giá trị False thường đc gọi là Falsy: 0, 0.0, 0j, None, set(), list[], dict{}, tuple(), ''

print(not 1)

# độ ưu tiên của toán tử: thực hiện trong dấu ngoặc trước 

# x = 6.1
# print(type(x))
# print(type(int(x)))

# user = input("nhap tuoi")
# print(type(user))
# print(int(user) + 5)

"""
    bài tập:
    - cho biết kiểu của các giá trị sau: -50, 4.98908, .5, 4+5j
    - định nghĩa 2 biến num1, num2 có cùng giá trị 1
    - nhập vào tên và tuổi và hiển thị ra màn hình, cách nhau bởi dấu phẩy
    - nhập vào 1 số nguyên, số thực, chuỗi và in các giá trị của chúng trên các dòng riêng biệt
"""

# kiểu string
# age = 30
# print("tui", age, "tuoi")

# print("tui {} tuoi".format(age))

food1 = "bun rieu"
food2 = "hu tieu"
food3 = "pho"

print("các món ăn như: ", food1,",", food2,",", food3, "được gọi là các món ăn sáng")

print("các món ăn như {0}, {2}, {1} được gọi là các món ăn sáng".format(food1, food2, food3))































