books = []


def add_book():
    try:
        book_id = input("Nhập mã sách: ")
        title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")
        quantity = int(input("Nhập số lượng: "))

        if quantity < 0:
            raise ValueError("Số lượng không được âm!")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "quantity": quantity
        }

        books.append(book)
        print("Thêm sách thành công!")

    except ValueError as e:
        print("Lỗi:", e)


def display_books():
    if len(books) == 0:
        print("Danh sách sách trống!")
        return

    print("\nDANH SÁCH SÁCH")
    for book in books:
        print(book)


def find_book():
    book_id = input("Nhập mã sách cần tìm: ")

    for book in books:
        if book["id"] == book_id:
            print(book)
            return

    print("Mã sách không tồn tại!")


def borrow_book():
    try:
        book_id = input("Nhập mã sách muốn mượn: ")

        for book in books:
            if book["id"] == book_id:

                if book["quantity"] == 0:
                    raise Exception("Sách đã hết!")

                book["quantity"] -= 1
                print("Mượn sách thành công!")
                return

        raise Exception("Mã sách không tồn tại!")

    except Exception as e:
        print("Lỗi:", e)


def return_book():
    try:
        book_id = input("Nhập mã sách muốn trả: ")

        for book in books:
            if book["id"] == book_id:
                book["quantity"] += 1
                print("Trả sách thành công!")
                return

        raise Exception("Mã sách không tồn tại!")

    except Exception as e:
        print("Lỗi:", e)


def delete_book():
    try:
        book_id = input("Nhập mã sách cần xóa: ")

        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                print("Xóa sách thành công!")
                return

        raise Exception("Mã sách không tồn tại!")

    except Exception as e:
        print("Lỗi:", e)


def sort_books():
    books.sort(key=lambda book: book["quantity"])
    print("Đã sắp xếp theo số lượng tăng dần!")


def main():
    while True:
        print("\n===== QUẢN LÝ THƯ VIỆN =====")
        print("1. Thêm sách")
        print("2. Hiển thị danh sách sách")
        print("3. Tìm sách theo mã")
        print("4. Mượn sách")
        print("5. Trả sách")
        print("6. Xóa sách")
        print("7. Sắp xếp theo số lượng")
        print("8. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            find_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            sort_books()
        elif choice == "8":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


main()