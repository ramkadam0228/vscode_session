import Image
import requests
from bs4 import BeautifulSoup

url='https://www.atyeti.com/'
response=requests.get(url)
print(response)
# print(response.content)
soup = BeautifulSoup(response.content,'html.parser')
# print(soap)
# headings=soup.find_all('h1')
# print(headings)
# headings=soup.find_all('h2')
# print(headings)
# headings=soup.find_all('h3')
# print(headings)
# headings=soup.find_all('h4')
# print(headings)
# headings=soup.find_all('h5')
headings=soup.find_all(['h1','h2','h3','h4','h5'])
# print(headings)

paragraphs=soup.find_all('paragraph')
print(paragraphs)


# links=soup.find_all('a')
# for link in links:
#     print(link)

links=soup.find_all('a')
# for link in links:
#     print(link.get('href'))



imgs=soup.find_all('img')
# for img in imgs:
#     print(img.get('src'))

# from urllib.parse import urljoin
# base_url='https://www.atyeti.com'
# for link in links:
#     href=urljoin(base_url,link.get('href'))
#     print(href)