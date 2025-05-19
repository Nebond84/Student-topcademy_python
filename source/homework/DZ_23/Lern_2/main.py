from book import Book

if __name__ == "__main__":
    title = input(f"Введите название: ")
    year = int(input(f"Введите год: "))
    publisher = input(f"Введите издательство")
    genre = input(f"Введите жанр: ")
    autor = input(f"Введите автора: ")
    price = float(input("Введите цену:"))

    book = Book(title= title,
                year= year,
                publisher= publisher,
                genre= genre,
                autor= autor,
                price= price)

    print(book.get_data())
