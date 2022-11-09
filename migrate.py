from dataclasses import _MISSING_TYPE
import databases
from json import loads, dumps
buildin_types = (int, float, str, tuple, list, dict)
types = {_type | type(None): _type for _type in buildin_types}
def main():
    db = input("Какую базу обновить?\n")
    to_update = databases.get_class_by_str(db)
    with open(f"{db}.json", "r", encoding="utf-8") as file:
        text = file.read()
        assert text, "Файл пуст"
        entries = loads(text)
    assert entries, "База пуста"
    old_fields = set(entries[0].keys())
    new_fields = set(to_update.fields().keys())
    
    for toadd in new_fields-old_fields:
        default = to_update.get_default(toadd)
        assert type(default) != _MISSING_TYPE, "Добавлено поле без значения по умолчанию"
        for entry in entries:
            entry[toadd] = default

    for todelete in old_fields-new_fields:
        for entry in entries:
            del entry[todelete]

    for entry in entries:
        for key in entry:
            field_type = to_update.get_type(key)
            if not isinstance(entry[key], field_type):
                if isinstance(field_type, type(int|str)):
                    field_type = types[field_type]
                try:
                    set_to = field_type(entry[key])
                except:
                    set_to = to_update.get_default(key)
                entry[key] = set_to

    with open(f"{db}.json", "w", encoding="utf-8") as file:
        file.write(dumps(entries))

if __name__ == "__main__":
    main()