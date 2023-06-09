import time
import logging

# Налаштування журналування
logging.basicConfig(filename='operational_log.log', level=logging.INFO, format='%(asctime)s %(message)s')


# Функція для реєстрації подій в Операційному Журналі
def log_event(user, event, level):
    logging.info(f"User: {user}, Event: {event}, Level: {level}")


# Функція для перевірки рівня небезпеки
def check_event_level(event):
    # Здесь можна реалізувати логіку перевірки рівня небезпеки для кожного типу події
    # Поверніть рівень небезпеки, відповідний події
    if event in ["error_login", "error_authentication"]:
        return 3
    elif event in ["access_denied", "encrypted_file_access"]:
        return 4
    elif event == "exceeded_privileges":
        return 2
    else:
        return 1


# Функція для обробки журналу за період часу
def process_log(log_file, user, U):
    # Зчитати файл журналу
    with open(log_file, 'r') as file:
        lines = file.readlines()

    # Змінні для підрахунку рівнів небезпеки
    levels = [0] * U

    # Проходимо по кожному рядку журналу
    for line in lines:
        # Розбити рядок на елементи
        timestamp, user, event = line.strip().split()

        # Перевірка рівня небезпеки події
        level = check_event_level(event)

        # Логування події
        log_event(user, event, level)

        # Підрахунок рівнів небезпеки
        if level <= U:
            levels[level - 1] += 1

    # Вивести результати
    for i, count in enumerate(levels):
        print(f"Level {i + 1}: {count} events")


# Приклад використання
def main():
    # Період часу Те = 1 день

    # Зчитування і обробка журналу за період часу
    process_log('operational_log.log', 'username', 3)


if __name__ == '__main__':
    main()
