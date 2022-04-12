import requests
import time
from threading import Thread

def get_html(link):
	text = requests.get(link).text
	print(f'{link} text length is {len(text)}')

links=['https://pythonru.com/', 'https://yandex.ru/', 'https://github.com/xrus92', 'https://brunoyam.com/', 'https://www.google.com/']
threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time() 
for t in threads:
	t.start()
	t.join()
print(f'Время последовательного выполнения: {time.time()-time1}\n')

threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
print(f'Время параллельного выполнения: {time.time()-time1}')