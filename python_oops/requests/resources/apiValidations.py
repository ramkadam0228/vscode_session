import requests
from collections.abc import Mapping

response = requests.get('http://216.10.245.166//Library/GetBook.php',params={'AuthorName':'Ram Kadam'},)
import json
# print(response.text)
# print(type(response.text))
dict_response=json.loads(response.text)

# print(dict_response[0])
# print(dict_response[0]['isbn'])
# json_respone=response.json()
# print(json_respone[0])
# print(response.status_code)
assert response.status_code == 200
# print(response.headers)

assert response.headers['Content-Type']=='application/json;charset=UTF-8'

# Retreive book etails

for book in dict_response:
    # print(type(book))
    if book['aisle'] == '2007':
        # print(book)
        break
expectedBook = {
    # 'book_name': 'Learn Appium Automation with Java', 'isbn': 'RAM', 'aisle': '2007'
    "book_name": "Learn Appium Automation with Java", "isbn": "RAM", "aisle": "2007"
}

# print(expectedBook)

assert book == expectedBook