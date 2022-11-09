import setup
import os
from dotenv import load_dotenv
import telebot
from json import loads, dumps
setup.main()

with open("requests.txt", "w", encoding="utf-8") as file: pass

def get_keyboard(to):
    if not os.path.exists(f"texts/keyboards/{to.lower()}"):
        return None
    keyboard = telebot.types.ReplyKeyboardMarkup(False, True)
    with open(f"texts/keyboards/{to.lower()}", "r", encoding="utf-8") as file:
        buttons = [line.split(";") for line in file]
    [keyboard.row(*line) for line in buttons if line]
    return keyboard

def get_answer(to):
    if not os.path.exists(f"texts/answers/{to.lower()}"):
        return None
    with open(f"texts/answers/{to.lower()}", "r", encoding="utf-8") as file:
        text, action, *_ = file.read().split("##")+[""]
    return text.strip(), action.strip()

def dialogue(message):
    try:
        reply = message.text
    except AttributeError:
        reply = message
    answer, action = get_answer(reply)
    if answer:
        bot.send_message(message.chat.id, answer, reply_markup=get_keyboard(reply))
    return action

def get_db(db):
    text = None
    while not text:
        with open(f"{db}.json", "r") as file:
            text = file.read()
    return loads(text)
def send_request(request):
    with open("requests.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{request}")

load_dotenv()
token = os.getenv("token")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_handler(message):
    dialogue("Hello")
    if not [entry for entry in get_db("User") if entry["chat_id"] == message.chat.id]:
        send_request(f"create_entry; User; {message.chat.id}")

@bot.message_handler(commands=["delete"])
def delete_handler(message):
    dialogue("Delete my data")
    send_request(f"delete_entry; User; {message.chat.id}")

def show_me(message):
    users = get_db("User")
    for user in users:
        if user["chat_id"] == message.chat.id:
            bot.send_message(message.chat.id, dumps(user))
            break

available_actions = {
    "show_me": show_me,
}
@bot.message_handler(content_types=["text"])
def text_handler(message):
    action = dialogue(message)
    available_actions[action](message)



bot.polling()