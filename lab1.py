# Перехоплення переривань та керування доступом до захищеного носія інформації

import getpass

# База даних користувачів
users = {
    "admin": {
        "password": "adm",
        "access_rights": "full"  # Повний доступ
    },
    "user1": {
        "password": "111",
        "access_rights": "limited"  # Обмежений доступ
    },
    "user2": {
        "password": "222",
        "access_rights": "limited"  # Обмежений доступ
    },
    "user3": {
        "password": "333",
        "access_rights": "limited"  # Обмежений доступ
    },
    "user4": {
        "password": "444",
        "access_rights": "limited"  # Обмежений доступ
    }
}


def authenticate():
    username = input("Введіть ім'я користувача: ")
    password = getpass.getpass(prompt="Введіть пароль: ")

    if username in users and users[username]["password"] == password:
        return users[username]["access_rights"]

    print("Не правильний пароль або ім'я користувача")
    return None


def access_disk(access_rights, disk):
    if access_rights == "full":
        print("Ви маєте повний доступ до диску")
        # Додатковий код для виконання операцій з диском
    elif access_rights == "limited":
        if disk.lower() == 'a' or disk.lower() == 'e':
            print("Ви маєте обмежений доступ до диску")
        else:
            print("Ви не маєте доступу до цього диску")
        # Додатковий код для виконання обмежених операцій з диском
    else:
        print("Невірні облікові дані або недостатньо прав доступу")


# Головна функція
def main():
    access_rights = authenticate()
    if access_rights is not None:
        disk = input("Введіть диск до якого хочете отримати доступ: ")
        access_disk(access_rights, disk)


# Виклик головної функції
main()
