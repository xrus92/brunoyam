import json
import os.path
def create_userdata():
	if not(os.path.isfile('userdata.json')):
		with open('userdata.json', 'w') as file:
			json.dump({'testlogin': 'testpassword'}, file)


def register(login, passwd):
	with open('userdata.json', 'r') as file:
		userdata = json.load(file)
	if login not in userdata.keys():
		userdata[login] = passwd
		with open('userdata.json', 'w') as file:
			json.dump(userdata, file)
		print('Вы успешно зарегестрированы!')
	else:
		print('Пользователь с таким логином уже существует!')


def login_function(login, passwd):
	with open('userdata.json', 'r') as file:
		userdata = json.load(file)
		if login in userdata.keys():
			if(userdata[login] == passwd):
				print('Успешный вход!')
			else:
				print('Неверный пароль!')
		else:
			print('Вы не зарегестрированы!')

create_userdata()
while True:
	print('вход или регистрация?: ')
	answer = str(input())
	if answer == 'вход':
		login_function(str(input('Введите логин: ')), str(input('Введите пароль: ')))
	elif answer == 'регистрация':
		register(str(input('Введите логин: ')), str(input('Введите пароль: ')))
	print('Начать заново? (да, нет): ')
	answer = str(input())
	if answer == 'да':
		continue
	elif answer == 'нет':
		break
	else:
		print('Нет, так нет...')
		break