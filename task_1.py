passwords = [
    "hello123",
    "mypassword",
    "123456",
    "python3.10",
    "pass word1",
    "qwerty",
    "secure2025",
    "letmein",
    "42isAnswer",
    "short"
]

for password in passwords:
    # Перевірка довжини
    if len(password) > 6:
        # Перевірка на наявність хоча б однієї цифри
        has_digit = any(char.isdigit() for char in password)
        
        # Перевірка, що немає пробілів
        no_spaces = " " not in password

        # Якщо виконуються всі умови — виводимо пароль
        if has_digit and no_spaces:
            print(password)
