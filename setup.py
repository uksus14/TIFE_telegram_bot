import os
from dotenv import load_dotenv
def check_dotenv():
    print("Проверяю наличие .env файла")
    if not os.path.exists(".env"):
        print(".env файл не найден")
        token = input("Введите токен телеграм бота\n")
        with open(".env", "w") as f:
            f.write(f'token = "{token}"\n')
        print("Токен установлен")
    else:
        print(".env файл найден")
        load_dotenv()
        token = os.getenv("token")
        if token is None:
            print("Токен телеграм бота не найден")
            token = input("Введите токен телеграм бота\n")
            with open(".env", "a") as f:
                f.write(f'token = "{token}"\n')
            print("Токен установлен")

def check_dotgitignore():
    print("Проверяю наличие .gitignore файла")
    if not os.path.exists(".gitignore"):
        print(".gitignore файл не найден")
        with open(".gitignore", "w") as f:
            f.write("*.env\n*.json\n")
        print(".gitignore файл создан")
    else:
        print(".gitignore файл найден")
        with open(".gitignore", "r") as f:
            ignored = set(f.read().split("\n"))
        if "*.env" not in ignored or "*.json" not in ignored:
            print("В .gitignore файле нет необходимых полей")
            ignored = ignored | {"*.env", "*.json"}
            with open(".gitignore", "w") as f:
                f.write("\n".join(ignored))
            print("Добавлено")

def check_user_db_json():
    print("Проверяю наличие базы данных")
    if not os.path.exists("user_db.json"):
        print("user_db.json файл не найден")
        with open("user_db.json", "w") as f:
            f.write("[]")
        print("user_db.json файл создан")
    else:
        print("user_db.json файл найден")

if __name__ == "__main__":
    check_dotenv()
    print()
    check_dotgitignore()
    print()
    check_user_db_json()
    print()