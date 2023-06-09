import math
import time

# База даних користувачів
import random

users = {
    "user1": {
        "password": "passwd1",
        "answers": ["Rose", "Juice"],
        "secret_func_value": 42
    },
    "user2": {
        "password": "passwd2",
        "answers": ["Tulip", "Water"],
        "secret_func_value": 73
    }
}

# Лічильник помилок
error_count = {}

# Інтервал часу (у секундах)
delta_t = 120

# Задавання питань або випадкових чисел
questions = ["Your favourite flower?", "Your favourite drink?"]


def authenticate(username, password):
    # Перевірка наявності користувача в базі даних
    if username in users:
        user = users[username]
        # Перевірка правильності пароля
        if password == user["password"]:
            return True
    return False


def ask_security_questions(user):
    for question in questions:
        answer = input(question + ": ")
        # Перевірка відповідей
        if answer not in user["answers"]:
            return False
    return True


def secret_function_authentication(user):
    # Генерація випадкового числа
    random_number = random.randint(1, 10)
    secret_value = user["secret_func_value"]
    # Обчислення секретної функції
    result = math.log10(secret_value * random_number)
    user_input = float(input("Enter the result of lg(a * x): "))
    # Перевірка обчисленого значення
    if user_input == result:
        return True
    return False


def registration():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    answers = []
    for i in range(2):
        answer = input(f"{questions[i]}")
        answers.append(answer)
    secret_value = float(input("Enter a value for the secret function: "))
    users[username] = {
        "password": password,
        "answers": answers,
        "secret_func_value": secret_value
    }
    error_count[username] = 0
    print("Registration successful!")


def main():
    operation = int(input("Choose an operation:\n1. Registration\n2. Authentication\nYour choice: "))
    if operation == 1:
        registration()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Аутентифікація користувача
        if authenticate(username, password):
            user = users[username]
            # Перевірка відповідей на контрольні питання
            if ask_security_questions(user):
                # Перевірка секретної функції
                if secret_function_authentication(user):
                    print("Authentication successful!")
                    break
                else:
                    print("Authentication failed. Please try again.")
            else:
                print("Authentication failed. Please try again.")
        else:
            print("Authentication failed. Please try again.")
        error_count[username] = error_count.get(username, 0) + 1
        # Перевірка кількості помилок
        if error_count[username] == 4:
            print("Maximum number of errors reached. Please contact the administrator for registration.")
            break
        # time.sleep(delta_t)  # Затримка на інтервал delta_t перед наступною спробою


if __name__ == "__main__":
    main()
