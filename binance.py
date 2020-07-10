import requests
from json import loads
from bs4 import BeautifulSoup
from typing import List
import time

def binance(link):
	try:
		base_url = f'{link}'
		request = requests.get(base_url)
		data = loads(request.text)
		print(data[0])

		f = open('one.txt', 'w', encoding='utf-8')

		f.write(f'''
	symbol: {data[0]['symbol']}
	ps: {data[0]['ps']}
	price: {data[0]['price']}
	time: {data[0]['time']}
	''')
		f.close()

	except:
		try:
			er = open('error_log.txt', 'a', encoding='utf-8')
		except Exception as e:
			er = open('error_log.txt', 'w', encoding='utf-8')
			er.write(e)
			er.close()

link = 'enter link of binance'

while True:
	binance(link)

	time.sleep(100)
