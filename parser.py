from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text()
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href
    })

f = open('text_site.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость №{i}\n\nНазвание: {item["title"]}\nКраткое описание: {item["desc"]}\nСсылка на новость: {item["href"]}\n\n*****************\n')
    i += 1