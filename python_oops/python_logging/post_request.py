import requests
 
url="http://127.0.0.1:5000/add"
payload={'a':10,'b':20}
response=requests.post(url,json=payload)
 
print('Response:',response.json())