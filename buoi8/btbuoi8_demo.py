# định nghĩa menu
USER_MENU = '''Nhập
a - thêm 1 bộ phim
l - hiển thị danh sách phim
s - tìm kiếm các bộ phim theo tên
x - xóa phim theo tên
u - cập nhật thông tin phim
q - thoát
Lựa chọn của bạn: '''

# Định nghĩa cấu trúc dữ liệu lưu trữ các bộ phim
# li1st[dict] mỗi 1 bộ phim là 1 dictionary nằm trong list
movies = []
# prevs: kiểm tra các bộ phim duy nhất
prevs = set()

# định nghĩa hàm xử lý
# thêm 1 bộ phim mới
def add_movie():
    # nhập thông tin bộ phim
    name = input('Nhập vào tên 1 bộ phim\t: ')
    while name in prevs:
        print('Tên phim bị trùng, vui lòng nhập lại')
        name = input('Nhập vào tên 1 bộ phim\t: ')
    director = input('Nhập vào tên đạo diễn\t: ')
    release_year = input('Nhập vào năm phát hành\t: ')

    # tạo bộ phim
    movie = {
        'name': name,
        'director': director,
        'release_year': release_year
    }
    movies.append(movie)
    prevs.add(name)

# hiển thị thông tin chi tiết
def show_movie(movie):
    movie_name = movie['name']
    movie_director = movie['director']
    movie_release_year = movie['release_year']

    print(f'Tên\t\t: {movie_name}')
    print(f'Đạo diễn\t\t: {movie_director}')
    print(f'Năm phát hành\t\t: {movie_release_year}')

# hiển thị các bộ phim
def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print("Thông tin bộ phim", idx)
            show_movie(movie)
    else:
        print('Danh sách phim trống')
    
# tìm kiếm phim theo tên
def search_movie():
    if movies:
        movie_name = input('Nhập tên bộ phim cần tìm: ')

        for idx, movie in enumerate(movies, start=1):
            if movie['name'] == movie_name:
                print('Thông tin bộ phim: ', idx)
                show_movie(movie)
                break
        else:
            print(f'Không tìm thấy thông tin bộ phim có tên là {movie_name}')
    else:
        print('Danh sách phim trống')

# xóa thông tin phim
def remove_movie():
    if movies:
        movie_name = input('Nhập tên bộ phim cần tìm: ')

        for idx, movie in enumerate(movies, start=1):
            if movie['name'] == movie_name:
                del movies[idx]
                print("Đã xóa")
                break
        else:
            print(f'Không tìm thấy thông tin bộ phim có tên là {movie_name}')
    else:
        print('Danh sách phim trống')

# cập nhật thông tin phim
def update_movie():
    if movies:
        movie_name = input('Nhập tên bộ phim: ')
        found = [
            idx
            for idx, movie in enumerate(movies)
            if movie['name'] == movie_name
        ]

        if found:
            position = found[0]
            movies[position]['director'] = ('Nhập vào tên đạo diễn\t: ')
            movies[position]['release_year'] = ('Nhập vào năm phát hành\t: ')
            print("Cập nhạt thành công")
        else:
            print(f'Không tìm thấy thông tin bộ phim có tên là {movie_name}')

    else:
        print('Danh sách phim trống')

# Lựa chọn
user_choice = input(USER_MENU)

# Định nghĩa dict chứa các lựa chọn
operations = {
    'a': add_movie,
    'l': show_movies,
    's': search_movie,
    'x': remove_movie,
    'u': update_movie
}

# Chọn nhiều operations cho đến khi hàm thoát
while user_choice != 'q':
    # kiểm tra tùy chọn có trong menu hay không
    # nếu có thì thực hiện, nếu không thì nhập lại
    if user_choice in operations:
        operations = operations[user_choice]
        operations()
    else:
        print("Lựa chọn không hợp lệ")

    user_choice = input(USER_MENU)
    