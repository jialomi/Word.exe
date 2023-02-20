import telebot
from telebot import types
from Script import bot, chat_id, is_running, check_multiplescripts, autoFarm
from Script import autoBR

@bot.message_handler(commands=['startFarm'])
def start_autoFarm(msg):
    global is_running 
    if check_multiplescripts() == True:
        if is_running[0] == True:
            bot.send_message(chat_id, 'autoFarm script is already running!')
        else:
            bot.send_message(chat_id, 'Other script(s) is already running!')
    else:
        is_running[0] = True
        bot.send_message(chat_id, 'autoFarm script started running!')
        autoFarm()

@bot.message_handler(commands=['stopFarm'])
def stop_autoFarm(msg):
    global is_running
    if is_running[0] == False:
        bot.send_message(chat_id, 'autoFarm script already stopped!')
    else:
        is_running[0] = False
        bot.send_message(chat_id, 'autoFarm script stopped!')

@bot.message_handler(commands=['startBR'])
def start_autoBR(msg):
    global is_running 
    if check_multiplescripts() == True:
        if is_running[1] == True:
            bot.send_message(chat_id, 'autoFarm script is already running!')
        else:
            bot.send_message(chat_id, 'Other script(s) is already running!')
    else:
        is_running[1] = True
        bot.send_message(chat_id, 'autoFarm script started running!')
        autoBR()

@bot.message_handler(commands=['stopBR'])
def stop_autoBR(msg):
    global is_running
    if is_running[1] == False:
        bot.send_message(chat_id, 'autoFarm script already stopped!')
    else:
        is_running[1] = False
        bot.send_message(chat_id, 'autoFarm script stopped!')

@bot.message_handler(commands=['status'])
def status_message(msg):
    message = "Scripts Status:\n"
    if is_running[0] == True:
        message += "AutoFarm status: Running\n"
    else:
        message += "AutoFarm status: Stopped\n"
    if is_running[1] == True:
        message += "AutoBR status: Running\n"
    else:
        message += "AutoBR status: Stopped\n"
    bot.send_message(chat_id, message)

@bot.message_handler(commands = ['close'])
def close_message(msg):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id=msg.chat.id, text="Closed", reply_markup = markup)


@bot.message_handler(commands = ['start'])
def start_whichScript(msg):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("/startFarm")
    btn2 = types.KeyboardButton("/stopFarm")
    btn3 = types.KeyboardButton("/startBR")
    btn4 = types.KeyboardButton("/stopBR")
    btn5 = types.KeyboardButton("/status")
    btn6 = types.KeyboardButton("/close")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    message = "Hello Please select which script you want to start/stop"
    bot.send_message(chat_id=msg.chat.id, text=message, reply_markup=markup)


bot.polling()
