import requests
# api_key = '0f60df0a3c505515436fea0e6239a1ca'
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0f60df0a3c505515436fea0e6239a1ca'
citys = ['india','London']
citys_temp = []

for city in citys:
	res = requests.get(url.format(city)).json()
	weather = {
	"city" : city,
	"temp" : res['main']['temp']
	}
	citys_temp.append(weather)
	# print(weather)
# print(citys_temp)
