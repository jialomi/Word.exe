import psutil
import telebot
import time
import os
import pyautogui
import io
import pygetwindow as gw
import keyboard

# Replace with your own Telegram bot token
bot = telebot.TeleBot("5839776788:AAGr8hhEHg_Qxmj_XSzlcLZ7Pm3McC7FlyQ")

# Replace with your own Telegram chat ID
chat_id = "301795147"

#Status to control script 
is_running = [False , False]

button_image = "C:/Users/Jeremy/Desktop/BR/button.png"

button_image2 = "C:/Users/Jeremy/Desktop/BR/button2.png"

def check_multiplescripts():

    global is_running
    found_true = False

    for i in range(len(is_running)):
        if is_running[i]:
            found_true = True
            break

    return found_true

def autoFarm():

    global is_running

    while True:
        
        if is_running[0] == False:
            break
        # Check if the game application is running
        if not any(proc.name() == "Trove.exe" for proc in psutil.process_iter()):
            # If the game application has crashed, send a notification to Telegram
            bot.send_message(chat_id, "Trove application has crashed!")
            os.system("taskkill /F /IM  cheatengine-x86_64-SSE4-AVX2.exe")
            Glyph = gw.getWindowsWithTitle('Glyph')[0]
            Glyph.activate()
            time.sleep(4)
            pyautogui.click(x=1739, y=340)
            time.sleep(5)
            if any(proc.name() == "Trove.exe" for proc in psutil.process_iter()):
                bot.send_message(chat_id, "Trove is now running")
                x = os.startfile('C:/Users/Jeremy/Downloads/word.CT')
                time.sleep(2)
                if x is not None:
                    bot.send_message(chat_id, "Failed to start auto farm")
                else:
                    troveWindow = gw.getWindowsWithTitle('Trove')[0]
                    troveWindow.resizeTo(1280,720)
                    troveWindow.moveTo(0,0)
                    bot.send_message(chat_id, "Successfully Started Engine")
                    time.sleep(3)
                    pyautogui.press('pagedown')
                    bot.send_message(chat_id, "Successfully Started Auto Farm")
                    time.sleep(15)
                    screenshot = pyautogui.screenshot()
                    buffer = io.BytesIO()
                    screenshot.save(buffer, format="PNG")
                    buffer.seek(0)
                    bot.send_photo(chat_id, photo=buffer)
            
        # Wait for 5 seconds before checking again
        time.sleep(5)

def autoBR():

    countBR = 0

    while True:

        if not any(proc.name() == "Trove.exe" for proc in psutil.process_iter()):

            bot.send_message(chat_id, 'Trove application has crashed!')
            time.sleep(1)
            pyautogui.click(x=313, y=1416)
            time.sleep(4)
            pyautogui.click(x=1760, y=345)
            time.sleep(3)
            troveWindow = gw.getWindowsWithTitle('Trove')[0]
            troveWindow.resizeTo(1280,720)
            troveWindow.moveTo(0,0)
            time.sleep(60)
            pyautogui.click(x=1030, y=90)

            if any(proc.name() == 'Trove.exe' for proc in psutil.process_iter()):
                bot.send_message(chat_id, "Trove has reopen and is now running")

                keyboard.press('ctrl')
                time.sleep(0.5)
                keyboard.press('b')
                time.sleep(0.5)
                keyboard.release('ctrl')
                keyboard.release('b')

                bot.send_message(chat_id, 'Auto BR has begun')

        button_pos = pyautogui.locateOnScreen(button_image)

        button_pos2 = pyautogui.locateOnScreen(button_image2)

        if button_pos is not None:

            countBR = countBR + 1

            if countBR % 5 == 0:

                bot.send_message(chat_id, f"You have done {countBR} BR since the script started")

            button_x, button_y = pyautogui.center(button_pos)

            pyautogui.click(button_x, button_y)

            time.sleep(3)

        if button_pos2 is not None:

            countBR = countBR + 1
            
            if countBR % 5 == 0:

                bot.send_message(chat_id, f"You have done {countBR} BR since the script started")

            button_x , button_y = pyautogui.center(button_pos2)

            pyautogui.click(button_x, button_y)

            time.sleep(3)