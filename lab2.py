import getpass
import datetime


def create_user():
    login = input("Enter login: ")
    password = getpass.getpass("Enter password: ")

    # Перевірка пароля на відповідність вимогам
    if not is_valid_password(password):
        print("Invalid password. Please choose a stronger password.")
        return

    # Отримання додаткових даних для аутентифікації
    name = input("Enter name: ")
    email = input("Enter email: ")
    role = input("Enter role: ")

    # Запис даних реєстрації в системний журнал
    registration_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{login},{password},{name},{email},{role},{registration_time}"
    append_to_journal(log_entry)

    print("User created successfully.")


def is_valid_password(password):
    min_length = 3
    if len(password) < min_length:
        return False

    return True


def append_to_journal(log_entry):
    with open("registration_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")


# Головна функція
def main():
    create_user()


# Виклик головної функції
if __name__ == "__main__":
    main()
