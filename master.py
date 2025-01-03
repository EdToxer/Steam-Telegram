import os
import telebot
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")
BOT_TOKEN = os.environ.get('BOT_TOKEN')

steam = Steam(KEY)
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я был создан пользователем EdCox, чтобы распространять казино и следить сколько часов в Доте 2. Команды: /dice <0-64> - Угадайте какое выпадет число в радиусе 5, /dota2 <стим_айди> - Количество часов за последние две недели, /steam <стим_айди> - Количество часов в играх за всю историю аккаунта")

@bot.message_handler(commands=["dice"])
def dice(message):
    bet = message.text.replace("/dice","")
    bet = bet.replace(" ","")
    try:
        print(bet)
        if not bet.isdigit() or (int(bet) > 64 or int(bet) < 0):
            msg = bot.reply_to(message, "Вводите вашу ставку при вызове бота от 0 до 64")
            return
        x = bot.send_dice(message.chat.id, "🎰")
        bot.send_message(message.chat.id, x.dice.value)
        if x.dice.value + 10 >= int(bet) and x.dice.value - 10 <= int(bet):
            bot.send_message(message.chat.id,"Вы победили!")
        else:
            bot.send_message(message.chat.id,"Вы проиграли!")
    except Exception as e:
        bot.reply_to(message, "Ууупс")

@bot.message_handler(commands=['dota2'])
def dota_check(message):
    enter = message.text.replace("/dota2","")
    enter = enter.replace(" ","")
    nickname = steam.users.get_user_details(str(enter))
    user = steam.users.get_user_recently_played_games(str(enter))
    i = 0
    result = 0
    GAME = 570
    recently_played_games = len(user["games"])
    while i < recently_played_games:
        if user["games"][i]["appid"] == GAME:
            result = user["games"][i]["playtime_2weeks"]
            i = recently_played_games
        else:
            i += 1
    bot.reply_to(message, str(result) + " - Количество минут в Доте 2 за две недели у пользователя - " + nickname["player"]["personaname"])

@bot.message_handler(commands=['steam'])
def steam_check(message):
    enter = message.text.replace("/steam","")
    enter = enter.replace(" ","")
    user = steam.users.get_owned_games(str(enter))
    nickname = steam.users.get_user_details(str(enter))
    i = 0
    result = 0
    recently_played_games = len(user["games"])
    while i < recently_played_games:
        result += user["games"][i]["playtime_forever"]
        i+=1
    bot.reply_to(message, nickname["player"]["personaname"] + " - наиграл за всё время: " + str(result//60) + " Часов или " + str(result//(60*24)) + " Дней" )

bot.infinity_polling()
