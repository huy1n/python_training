""" SQLite 
1:1
1:n
n:n

"""
# SQLite là file có đuôi .db
import sqlite3

conn = sqlite3.connect("moviess.db")

cur = conn.cursor()

# sql_conmmand = """
# CREATE TABLE IF NOT EXISTS movie (
#     title TEXT,
#     year INTEGER,
#     score REAL
# );
# """
# cur.execute(sql_conmmand)

# sql_conmmand = """
# INSERT INTO movie VALUES
# ('mr. boot', 1998, 9.2),
# ('mr. ring', 1999, 9.1),
# ('mr. hat', 1978, 7.2);
#  """

sql_command = "SELECT * FROM movie;"

sql_command = """
UPDATE movie
SET year = 2000
WHERE title = 'mr. boot';
"""

sql_command = """
DELETE FROM movie;
"""

cur.execute(sql_command)

# lay dong
""" lst = cur.fetchall()
print(lst)

for line in cur:
    print(line) """

conn.commit()  # dùng để xác nhận sự thay đổi của CSDL


conn.close()

""" bài tập:
tạo 1 chương trình CRUD (create - read - update - delete) sử dụng sqlite3 trong python trên 1 bảng book(id, name, author) với id là khóa chính thuộc kiểu integer tự động tăng giá trị mỗi khi 1 bản ghi được thêm vào
 """
