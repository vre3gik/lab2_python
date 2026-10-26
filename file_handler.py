from password_checker import find_passwords


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return None

    except UnicodeError:
        print("Ошибка: не удалось прочитать кодировку файла.")
        return None

    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
        return None


def check_file(filename):
    text = read_file(filename)
    if text is None:
        return None

    passwords = find_passwords(text)
    return passwords
