import unittest
from unittest.mock import patch, mock_open, Mock

from password_checker import check_password, find_passwords
from file_handler import check_file
from web_handler import check_website


class TestPasswordChecker(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(check_password("Hello123!"))

    def test_short_password(self):
        self.assertFalse(check_password("Hi1!"))

    def test_no_uppercase(self):
        self.assertFalse(check_password("hello123!"))

    def test_no_lowercase(self):
        self.assertFalse(check_password("HELLO123!"))

    def test_no_digits(self):
        self.assertFalse(check_password("HelloWorld!"))

    def test_no_special_characters(self):
        self.assertFalse(check_password("Hello1234"))

    def test_password_with_spaces(self):
        self.assertFalse(check_password("Hello 123!"))

    def test_long_password(self):
        self.assertFalse(check_password("Hello123456789012345!"))

    def test_empty_password(self):
        self.assertFalse(check_password(""))

    def test_valid_length_boundaries(self):
        self.assertTrue(check_password("Abcdef1!"))
        self.assertTrue(check_password("Abcdefghijklmnopq1!@"))

    def test_invalid_characters(self):
        self.assertFalse(check_password("Hello123!?"))
        self.assertFalse(check_password("Пароль123!"))

    def test_find_passwords(self):
        text = "Hello123! qwerty Test456@"
        result = find_passwords(text)
        self.assertEqual(result, ["Hello123!", "Test456@"])

    def test_no_passwords_found(self):
        text = "hello qwerty password"
        result = find_passwords(text)
        self.assertEqual(result, [])

    def test_password_boundaries(self):
        text = "abcHello123!xyz"
        result = find_passwords(text)
        self.assertEqual(result, [])

    def test_find_passwords_in_file(self):
        text = "Hello123! qwerty Test456@"
        with patch(
                "builtins.open",
                mock_open(read_data=text)
        ):
            result = check_file("passwords.txt")
        self.assertEqual(result, ["Hello123!", "Test456@"])

    def test_file_not_found(self):
        with patch(
                "builtins.open",
                side_effect=FileNotFoundError
        ):
            result = check_file("missing.txt")
        self.assertIsNone(result)

    @patch("web_handler.requests.get")
    def test_find_passwords_on_website(self, mock_get):
        response = Mock()
        response.text = "<p>Hello123! qwerty Test456@</p>"
        response.raise_for_status.return_value = None
        mock_get.return_value = response
        result = check_website("https://example.com")
        self.assertEqual(result, ["Hello123!", "Test456@"])

    @patch("web_handler.requests.get")
    def test_website_error(self, mock_get):
        import requests
        mock_get.side_effect = requests.RequestException(
            "Ошибка соединения"
        )
        result = check_website("https://example.com")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
