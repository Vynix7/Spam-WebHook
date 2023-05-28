import time
import requests
import colorama
import os

os.system("color 1")
os.system("pip install time")
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install os")
os.system("cls")
os.system("title Gang-Raid ::: Made By Vynix")

colorama.init()

print(colorama.Fore.LIGHTCYAN_EX + "   /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$          /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$ ")
print("  /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$        | $$__  $$ /$$__  $$|_  $$_/| $$__  $$")
print(" | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/        | $$  \ $$| $$  \ $$  | $$  | $$  \ $$")
print(" | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$ /$$$$$$| $$$$$$$/| $$$$$$$$  | $$  | $$  | $$")
print(colorama.Fore.CYAN + " | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$|______/| $$__  $$| $$__  $$  | $$  | $$  | $$")
print(" | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$        | $$  \ $$| $$  | $$  | $$  | $$  | $$")
print(" |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/        | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/")
print("  \______/ |__/  |__/|__/  \__/ \______/         |__/  |__/|__/  |__/|______/|_______/ ")
print(colorama.Fore.LIGHTWHITE_EX + "")

colorama.init()

msg = input("Your Spam Message : ")
webhook = input("webhook URL: ")
def spam(msg, webhook):
     for i in range(30):
         try:   
             data = requests.post(webhook, json={'content': msg})
             if data.status_code == 204:           
                 print(f"Sent MSG {msg}")
         except:
             print("Bad Webhook :" + webhook)
             time.sleep(5)
             exit()
counts = 1
while counts == 1:
    spam(msg, webhook)