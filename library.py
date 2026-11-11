"""Интерактивное приложение для управления небольшой библиотекой."""


def is_yes(answer: str) -> bool:
    """Проверяет, является ли ответ пользователя положительным."""
    return answer.strip().casefold() in {"да", "д", "yes"}


def add_books(library: dict[str, list[str]]) -> None:
    """Добавляет новые книги в библиотеку. Изменяет переданный словарь на месте."""
    while is_yes(input("Готов добавить новую книгу? (да/нет): ")):
        author = input("Введи фамилию автора: ").strip()
        title = input("Введи название книги: ").strip()

        if not author or not title:
            print("Автор и название книги не должны быть пустыми.")
            continue

        books = library.setdefault(author, [])

        if title in books:
            print("Такая книга уже есть в библиотеке.")
            continue

        books.append(title)
        print(f"Книга «{title}» добавлена.")


def show_author_books(library: dict[str, list[str]]) -> None:
    """Показывает книги выбранных пользователем авторов."""
    if not is_yes(input("Хочешь посмотреть книги какого-нибудь автора? (да/нет): ")):
        return

    while True:
        author = input("Введи фамилию автора: ").strip()

        if author in library:
            print(f"Книги автора {author}: {', '.join(library[author])}")
        else:
            print("Такого автора нет в библиотеке.")

        if not is_yes(input("Хочешь посмотреть книги другого автора? (да/нет): ")):
            break


def show_library(library: dict[str, list[str]]) -> None:
    """Выводит всех авторов и их книги в алфавитном порядке."""
    for author in sorted(library):
        books = ", ".join(sorted(library[author]))
        print(f"{author}: {books}")


def find_author_with_most_books(
    library: dict[str, list[str]],
) -> str | None:
    """Возвращает имя автора с наибольшим количеством книг. Если библиотека пуста, возвращает None."""
    return max(library, key=lambda author: len(library[author]), default=None)


def main() -> None:
    """Запускает программу управления библиотекой."""
    library = {
        "Достоевский": ["Преступление и наказание", "Идиот"],
        "Толстой": ["Война и мир", "Анна Каренина"],
        "Булгаков": ["Мастер и Маргарита"],
    }

    print("Привет! Добро пожаловать в электронную библиотеку.")

    while True:
        add_books(library)
        show_author_books(library)

        if is_yes(input("Хочешь увидеть все книги в библиотеке? (да/нет): ")):
            show_library(library)

        if is_yes(
            input("Хочешь узнать, у какого автора больше всего книг? (да/нет): ")
        ):
            author = find_author_with_most_books(library)

            if author is None:
                print("Библиотека пока пуста.")
            else:
                print(f"Автор с наибольшим количеством книг в библиотеке: {author}.")

        if is_yes(input("Хочешь завершить работу программы? (да/нет): ")):
            print("Спасибо за использование электронной библиотеки! До встречи!")
            break

        print("Хорошо, продолжаем работу с библиотекой!\n")


if __name__ == "__main__":
    main()
