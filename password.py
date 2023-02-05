import secrets


# Функция получает на вход длину пароля и используемые символы в виде строки
# для выбора случайного символа используем метод CHOICE библиотеки secrets
def create_new(length, characters):
    return ''.join(secrets.choice(characters) for _ in range(length))
