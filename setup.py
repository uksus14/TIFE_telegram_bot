import os
from dotenv import load_dotenv
from databases import get_all_classes
def check_dotenv():
    print("Проверяю наличие .env файла")
    if not os.path.exists(".env"):
        print(".env файл не найден")
        token = input("Введите токен телеграм бота\n")
        with open(".env", "w") as file:
            file.write(f'token = "{token}"\n')
        print("Токен установлен")
    else:
        print(".env файл найден")
        load_dotenv()
        token = os.getenv("token")
        if token is None:
            print("Токен телеграм бота не найден")
            token = input("Введите токен телеграм бота\n")
            with open(".env", "a") as file:
                file.write(f'token = "{token}"\n')
            print("Токен установлен")

def check_dotgitignore():
    print("Проверяю наличие .gitignore файла")
    if not os.path.exists(".gitignore"):
        print(".gitignore файл не найден")
        with open(".gitignore", "w") as file:
            file.write("*.env\n*.json\n")
        print(".gitignore файл создан")
    else:
        print(".gitignore файл найден")
        with open(".gitignore", "r") as file:
            ignored = set(file.read().split("\n"))
        if {"*.env", "*.json", "requests.txt"} - ignored:
            print("В .gitignore файле нет необходимых полей")
            ignored = ignored | {"*.env", "*.json"}
            with open(".gitignore", "w") as file:
                file.write("\n".join(ignored))
            print("Добавлено")

def check_user_db_json():
    print("Проверяю наличие баз данных")
    for db in get_all_classes():
        if not os.path.exists(f"{db}.json"):
            print(f"{db}.json файл не найден")
            with open(f"{db}.json", "w") as file:
                file.write("[]")
            print(f"{db}.json файл создан")
        else:
            print(f"{db}.json файл найден")
        print()

def main():
    check_dotenv()
    print("-"*30)
    check_dotgitignore()
    print("-"*30)
    check_user_db_json()
    print("-"*30)

if __name__ == "__main__":
    main()