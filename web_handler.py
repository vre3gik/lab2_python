import requests

from password_checker import find_passwords


def get_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.RequestException as error:
        print(f"Ошибка загрузки страницы: {error}")
        return None


def check_website(url):
    text = get_webpage(url)
    if text is None:
        return None

    passwords = find_passwords(text)
    return passwords
