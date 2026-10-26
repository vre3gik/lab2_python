from password_checker import check_password
from file_handler import check_file
from web_handler import check_website


def show_passwords(passwords):
    if passwords is None:
        return
    if passwords:
        print("\nНайденные надежные пароли:")

        for password in passwords:
            print(password)
    else:
        print("\nНадежные пароли не найдены.")


def main():
    while True:
        print("\nПРОВЕРКА НАДЕЖНОСТИ ПАРОЛЕЙ")
        print("1. Проверить введенный пароль")
        print("2. Найти пароли в файле")
        print("3. Найти пароли на веб-странице (можно использовать тестовый сайт)")
        print("4. Выход")
        choice = input("\nВыберите действие: ")

        if choice == "1":
            password = input("Введите пароль: ")
            if check_password(password):
                print("Пароль надежный!")
            else:
                print("Пароль ненадежный!")

        elif choice == "2":
            filename = input("Введите имя файла: ")
            passwords = check_file(filename)
            show_passwords(passwords)


        elif choice == "3":
            test_url = "https://vre3gik.github.io/lab2_python/"
            print("\nДля проверки можно использовать тестовый сайт:")
            print(test_url)
            url = input("\nВведите URL сайта (Enter — тестовый сайт): ")
            if not url:
                url = test_url
            passwords = check_website(url)
            show_passwords(passwords)

        elif choice == "4":
            print("Программа завершена, thanks for attention")
            break
        else:
            print("Ошибка! Выберите пункт от 1 до 4.")


if __name__ == "__main__":
    main()
