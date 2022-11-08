from dataclasses import _MISSING_TYPE
import databases
from json import loads, dumps
def main():
    db = input("Какую базу обновить?\n")
    to_update = databases.get_class_by_str(db)
    with open(f"{db}.json", "r") as file:
        entries = loads(file.read())
    if not entries:
        print("База пуста")
        quit()
    old_fields = set(entries[0].keys())
    new_fields = set(to_update.fields().keys())
    
    for toadd in new_fields-old_fields:
        default = to_update.get_default(toadd)
        if type(default) == _MISSING_TYPE:
            print("Добавлено поле без значения по умолчанию")
            continue
        for entry in entries:
            entry[toadd] = default

    for todelete in old_fields-new_fields:
        for entry in entries:
            del entry[todelete]

    for entry in entries:
        for key in entry:
            field_type = to_update.get_type(key)
            if not isinstance(entry[key], field_type):
                entry[key] = to_update.get_default(key)

    with open(f"{db}.json", "w") as file:
        file.write(dumps(entries))

if __name__ == "__main__":
    main()