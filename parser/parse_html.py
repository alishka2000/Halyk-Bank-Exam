from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://fckairat.com/news"  # Вводите url страницы которую хотите запарсить
page = urlopen(url)
html = page.read().decode("utf-8")

# Используя библиотеку BeautifulSoup выводим информацию в более красивом виде
soup = BeautifulSoup(html, "html.parser")
news = soup.find_all(class_='news-list')

# Создаем пустой list для записи наших новостей
results = []

# Делаем цикл, чтобы вывелось не только 1 новость
for item in news:
    title = item.find("div", class_='ltext').getText()  # Находим заголовок по тегам
    description = item.find("div", class_='ltext2').getText()  # Находим описание по тегам
    href = item.a.get('href')  # Находим ссылку новости
    #  Добавляем информацию в наш list
    results.append({
        'title': title,
        'description': description,
        'href': href
    })

# Создаем текстовый документ для записании нашего list-а
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость №{i}\n\nНазвание: {item["title"]}\n'
            f'Описание: {item["description"]}\n'
            f'Ссылка: {item["href"]}\n\n*********************\n')
    i += 1
f.close()

'''
    Также можно было бы по пагинации выводит информацию, но для этого нужно чуть больше времени)))
'''
