import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    price = book.find('p', class_='price_color').text
    if float(price.replace('£', '')) > 30:
        continue
    title = book.h3.a['title']
    rating = book.find('p', class_='star-rating')['class'][1]
    availability = book.find('p', class_='availability').text.strip()
    link = book.find('div', class_='image_container').a['href']
    full_link = url + link

    print(f'Title: {title}')
    print(f'Rating: {rating}')
    print(f'Price: {price}')
    print(f'Availability: {availability}')
    print(f'Link: {full_link}')
    print('-'*30)