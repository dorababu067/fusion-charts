import requests
url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey=4672ca9f464d483fa7d83713e67a0b2f'
countrys = ['in','us','gb']
latest_news = []

for country in countrys:
	data = requests.get(url.format(country)).json()
	if country == 'in':
		news = {
			"news" :  data['articles'][0]['title'],
			"url"  :  data['articles'][0]['url']
		}
		latest_news.append(news)
	elif country == 'us':
		news = {
			"news" :  data['articles'][0]['title'],
			"url"  :  data['articles'][0]['url']
		}
		latest_news.append(news)
	elif country == 'ua':
		news = {
			"news" :  data['articles'][0]['title'],
			"url"  :  data['articles'][0]['url']
		}
		latest_news.append(news)
			
# print(latest_news)