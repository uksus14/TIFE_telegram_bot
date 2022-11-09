from time import sleep
from json import loads, dumps
from databases import get_class_by_str

def read_entries(db):
    with open(f"{db}.json", "r", encoding="utf-8") as file:
        entries = loads(file.read())
    return entries
def write_entries(db, entries):
    with open(f"{db}.json", "w", encoding="utf-8") as file:
        file.write(dumps(entries))

def create_entry(db, *properties):
    entries = read_entries(db)
    last = max([entry["id"] for entry in entries]+[-1])
    entries.append(get_class_by_str(db)(last+1, *properties).to_dict())
    write_entries(db, entries)

def delete_entry(db, id):
    entries = read_entries(db)
    entries = [entry for entry in entries if entry["id"] != id]
    write_entries(db, entries)
    
def modify_entry(db, id, change):
    entries = read_entries(db)
    to_change = [entry for entry in entries if entry["id"] == int(id)][0]
    to_change.update(loads(change))
    write_entries(db, entries)

processes = {
    "create_entry": create_entry,
    "delete_entry": delete_entry,
    "modify_entry": modify_entry,
}
seconds_to_update = .1
def main():
    with open("requests.txt", "r", encoding="utf-8") as file:
        lines_was = len(file.read().split("\n"))

    for _ in range(10*60*60*24):
        with open("requests.txt", "r", encoding="utf-8") as file:
            requests = file.read().split("\n")
        todo = requests[lines_was:]
        for request in todo:
            if not request: continue
            action, *properties = [word.strip() for word in request.split(";")]
            processes[action](*properties)
        lines_was = len(requests)
        sleep(seconds_to_update)

    with open("requests.txt", "w", encoding="utf-8") as file:
        pass

if __name__ == "__main__":
    while True:
        main()