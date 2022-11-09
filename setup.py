import os
from dotenv import load_dotenv
from databases import get_all_classes
def check_dotenv():
    print("Проверяю наличие .env файла")
    if not os.path.exists(".env"):
        print(".env файл не найден")
        token = input("Введите токен телеграм бота\n")
        with open(".env", "w", encoding="utf-8") as file:
            file.write(f'token = "{token}"\n')
        print("Токен установлен")
    else:
        print(".env файл найден")
        load_dotenv()
        token = os.getenv("token")
        if token is None:
            print("Токен телеграм бота не найден")
            token = input("Введите токен телеграм бота\n")
            with open(".env", "a", encoding="utf-8") as file:
                file.write(f'token = "{token}"\n')
            print("Токен установлен")

def check_user_db_json():
    print("Проверяю наличие баз данных")
    for db in get_all_classes():
        if not os.path.exists(f"{db}.json"):
            print(f"{db}.json файл не найден")
            with open(f"{db}.json", "w", encoding="utf-8") as file:
                file.write("[]")
            print(f"{db}.json файл создан")
        else:
            print(f"{db}.json файл найден")
            with open(f"{db}.json", "r", encoding="utf-8") as file:
                data = file.read()
            if data[:1]+data[-1:] != "[]":
                ans = input(f"{db}.json файл повреждён или пуст, исправить(Y/n)? (Это очистит файл)\n")
                if ans == "Y":
                    with open(f"{db}.json", "w", encoding="utf-8") as file:
                        file.write("[]")
        print()

def main():
    check_dotenv()
    print("-"*30)
    check_user_db_json()
    print("-"*30)
    print("Развёртка закончена")

if __name__ == "__main__":
    main()