""" bài tập:
tạo 1 chương trình CRUD (create - read - update - delete) sử dụng sqlite3 trong python trên 1 bảng book(id, name, author) với id là khóa chính thuộc kiểu integer tự động tăng giá trị mỗi khi 1 bản ghi được thêm vào
 """
import sqlite3

conn = sqlite3.connect("books.db")

cur = conn.cursor() # tạo ra 1 con trỏ (cursor) để thực hiện các câu lệnh SQL

sql_command = """ 
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL
);
 """
# cach 1
# sql_command = """ 
# INSERT INTO books (name, author) VALUES
# ('dark people heart', 'tui'),
# ('sach 1', 'van la tui'),
# ('sach 2', 'tui 3')
# ;
#  """
# cach 2
sql_command = """ 
INSERT INTO books (name, author) VALUES (?, ?)
 """

lst = [
    ('dark people heart 1 ', 'tui'),
    ('sach 1 2', 'van la tui'),
    ('sach 2 3', 'tui 3')
]

# cach 1
# cur.execute(sql_command, lst) # thực thi lệnh SQL thông qua biến sql_command
# cach 2
conn.executemany(sql_command, lst)
conn.commit() # xác nhận sự thay đổi

conn.close()
