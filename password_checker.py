import re

PASSWORD_PATTERN = (
    r"(?<![A-Za-z0-9!@#$%^&*])"
    r"(?=[A-Za-z0-9!@#$%^&*]{8,20}(?![A-Za-z0-9!@#$%^&*]))"
    r"(?=[A-Za-z0-9!@#$%^&*]*[A-Z])"
    r"(?=[A-Za-z0-9!@#$%^&*]*[a-z])"
    r"(?=[A-Za-z0-9!@#$%^&*]*\d)"
    r"(?=[A-Za-z0-9!@#$%^&*]*[!@#$%^&*])"
    r"[A-Za-z0-9!@#$%^&*]+"
    r"(?![A-Za-z0-9!@#$%^&*])"
)

password_regex = re.compile(PASSWORD_PATTERN)


def check_password(password):
    if password_regex.fullmatch(password):
        return True

    return False


def find_passwords(text):
    return password_regex.findall(text)
