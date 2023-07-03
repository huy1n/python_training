""" 
OOP
"""

# self là tham số mặc định ở mọi hàm trong class
""" class Student:
    # contruction function: hàm khởi tạo
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        print(f'''Student Info
Name: {self.name}
Age: {self.age}
Address: {self.address}''')

    # dunder method
    def __str__(self):
        return f"<Student(name = {self.name}, age = {self.age})>"
    
    def __gt__(self, other):
        return self.age > other.age


student_one = Student('bob', 23, "NYC")

student_one.show_info()
print()
Student.show_info(student_one)
 """

""" class Human:
    def __init__(self, birth):
        self.birth = birth

    @property #coi get_birth la 1 cai thuoc tinh cua Human
    # day la decorator nhan vao 1 ham va tra ve 1 ham khac
    # chi duoc su dung khi ham co 1 tham so self
    def get_birth(self):
        return 2023 - self.birth



people_one = Human(2002)
# khi khong co property
# age = people_one.get_birth()
# khi co property
age = people_one.get_birth

print(age) """

""" class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

# ke thua
class Student(Human):
    def __init__(self, name, age):
        super().__init__(name) # super là lời gọi class Human
        self.age = age

    def __str__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}'
    
# nếu class Student không có str thì sẽ gọi str của parent 
student1 = Student('huy', 21)
print(student1) """

class Student1:
    def __init__(self, name = "bob"):
        self.name = name
    
    def __repr__(self):
        return f'<Student (Name = {self.name})>'
    
    def __str__(self):
        return f'Name: {self.name}'
    
s1 = Student1()
s2 = Student1('joe')
print(s2.name)
print(s1.name)

# trong python mọi thứ đều hoạt động dựa trên dunder
print(s1)
print(repr(s2))
print(s1.__str__())
print(str(s2))

class Student:
    # đếm số đối tượng đc khởi tạo
    count = 0
    def __init__(self):
        Student.count += 1

student1 = Student()
student2 = Student()
print(Student.count)



""" File

Open
Process
Close

 """

""" data = open('test.txt', mode='r') #mode w để ghi

read = data.read()
print(data) 

data.close() """

fp = open('test.txt', mode = 'w')

fp.write('kenny')

fp.close()